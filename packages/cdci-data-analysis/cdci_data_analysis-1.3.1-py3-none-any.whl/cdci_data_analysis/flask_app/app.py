#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:55:20 2017

@author: Andrea Tramcere, Volodymyr Savchenko
"""
from builtins import (open, str, range,
                      object)
from collections import Counter, OrderedDict
import copy
from werkzeug.utils import secure_filename

import os
import glob
import string
import random
from raven.contrib.flask import Sentry

import traceback

from flask import jsonify, send_from_directory, redirect, Response
from flask import Flask, request, make_response, abort, g
from flask.json import JSONEncoder
from flask_restx import Api, Resource, reqparse


import tempfile
import tarfile
import gzip
import logging
import socket
import logstash
import time as _time


from ..plugins import importer

from ..analysis.queries import *
from ..analysis.job_manager import Job, job_factory
from ..analysis.io_helper import FilePath, FitsFile
from .mock_data_server import mock_query
from ..analysis.products import QueryOutput
from ..configurer import DataServerConf
from ..analysis.plot_tools import Image
from .dispatcher_query import InstrumentQueryBackEnd
from ..analysis.exceptions import APIerror, BadRequest
from ..app_logging import app_logging
from . import tasks

from ..analysis.json import CustomJSONEncoder

from cdci_data_analysis import __version__
import oda_api

from astropy.io.fits.card import Undefined as astropyUndefined


#UPLOAD_FOLDER = '/path/to/the/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'fits', 'fits.gz'])

logger = app_logging.getLogger('flask_app')


app = Flask(__name__,
            static_url_path=os.path.abspath('./'),
            static_folder='/static')

app.json_encoder = CustomJSONEncoder


api = Api(app=app, version='1.0', title='CDCI ODA API',
          description='API for ODA CDCI dispatcher microservices\n Author: Andrea Tramacere, Volodymyr Savchenko')


ns_conf = api.namespace('api/v1.0/oda', description='api')


@app.before_request
def before_request():
    g.request_start_time = _time.time()


@app.route("/api/meta-data")
def run_api_meta_data():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_meta_data()


@app.route("/api/parameters")
def run_api_parameters():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_paramters_dict()


@app.route("/api/instr-list")
def run_api_instr_list():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_instr_list()


@app.route('/meta-data')
def meta_data():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_meta_data()


@app.route('/api/par-names')
def get_api_par_names():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_api_par_names()


@app.route('/check_satus')
def check_satus():
    par_dic = {}
    par_dic['instrument'] = 'mock'
    par_dic['query_status'] = 'new'
    par_dic['session_id'] = u''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(16))
    par_dic['job_status'] = 'submitted'
    query = InstrumentQueryBackEnd(
        app, par_dic=par_dic, get_meta_data=False, verbose=True)
    print('request', request.method)
    return query.run_query_mock()


@app.route('/meta-data-src')
def meta_data_src():
    query = InstrumentQueryBackEnd(app, get_meta_data=True)
    return query.get_meta_data('src_query')


@app.route("/download_products", methods=['POST', 'GET'])
def download_products():
    #instrument_name = 'ISGRI'
    query = InstrumentQueryBackEnd(app)
    return query.download_products()


@app.route('/test', methods=['POST', 'GET'])
def run_analysis_test():
    query = InstrumentQueryBackEnd(app)
    return query.run_query()


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(APIerror)
def handle_bad_request(error):
    response = jsonify({**error.to_dict(),
                        'error': str(error) + ':' + error.message,
                        **common_exception_payload()})
    response.status_code = error.status_code
    return response


def remove_nested_keys(D, keys):
    if isinstance(D, dict):
        return {k: remove_nested_keys(v, keys) for k, v in D.items() if k not in keys}

    if isinstance(D, list):
        return [remove_nested_keys(v, keys) for v in D]

    if isinstance(D, tuple):
        return tuple([remove_nested_keys(v, keys) for v in D])

    return D


def common_exception_payload():
    payload = {}

    payload['cdci_data_analysis_version'] = __version__
    payload['oda_api_version'] = oda_api.__version__
    _l = []

    for instrument_factory in importer.instrument_factory_list:
        _l.append('%s' % instrument_factory().name)

    payload['installed_instruments'] = _l

    payload['debug_mode'] = os.environ.get(
        'DISPATCHER_DEBUG_MODE', 'yes')  # change the default

    if payload['debug_mode'] == "yes":
        payload['config'] = {
            'dispatcher-config': remove_nested_keys(app.config['conf'].as_dict(),
                                                    ['sentry_url', 'logstash_host', 'logstash_port', 'secret_key',
                                                     'smtp_server_password'])
        }

    plugins = {}
    payload['config']['plugins'] = plugins
    for plugin_name, plugin_module in importer.cdci_plugins_dict.items():
        plugins[plugin_name] = {
            'config_file': plugin_module.conf_file
        }

    return payload


@app.route('/run_analysis', methods=['POST', 'GET'])
def run_analysis():
    """
    DRAFT
    ---
    operationId: 'run_analysis'
    parameters:
    - name: 'query_status'
      in: 'query'
      required: false
      type: 'string'
    responses:
        200: 
            description: 'analysis done'
        202: 
            description: 'request accepted but not done yet' 
        400: 
            description: 'something in request not understood - missing, unexpected values'
    """
    try:
        # t0 = _time.time()
        t0 = g.request_start_time
        query = InstrumentQueryBackEnd(app)
        r = query.run_query(disp_conf=app.config['conf'])
        logger.info("run_analysis for %s took %g seconds", request.args.get(
            'client-name', 'unknown'), _time.time() - t0)

        return r
    except APIerror as e:
        raise
    except Exception as e:
        logging.getLogger().error("exception in run_analysis: %s %s",
                                  repr(e), traceback.format_exc())
        print("exception in run_analysis: %s %s",
              repr(e), traceback.format_exc())

        raise InvalidUsage('request not valid',
                           status_code=410,
                           payload={'error_message': str(e), **common_exception_payload()})


@app.route('/test_mock', methods=['POST', 'GET'])
def test_mock():
    # instrument_name='ISGRI'
    query = InstrumentQueryBackEnd(app)
    return query.run_query_mock()


@app.route('/call_back', methods=['POST', 'GET'])
def dataserver_call_back():
    #log = logging.getLogger('werkzeug')
    #log.disabled = True
    #app.logger.disabled = True
    print('===========================> dataserver_call_back')
    query = InstrumentQueryBackEnd(
    # TODO get rid of the mock instrument
        app, instrument_name='mock', data_server_call_back=True)
    query.run_call_back()
    print('===========================>\n\n\n')
    return jsonify({})


####################################### API #######################################


@api.errorhandler(APIerror)
def handle_api_error(error):
    print("=> APIerror flask handler", error)
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# TODO: apparently flask-restplus modifies (messes up) error handling of flask.
# since it's deprecated and to be removed, no reason to try figuring it out


@api.errorhandler(Exception)
def handle_error(error):
    print("=> APIerror flask handler", error)
    return make_response(f"unmanagable error: {error}"), 400


def output_html(data, code, headers=None):
    resp = Response(data, mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp


@ns_conf.route('/product/<path:path>', methods=['GET', 'POST'])
# @app.route('/product/<path:path>',methods=['GET','POST'])
class Product(Resource):
    @api.doc(responses={410: 'problem with local file delivery'}, params={'path': 'the file path to be served'})
    def get(self, path):
        """
        serves a locally stored file
        """
        try:
            return send_from_directory(os.path.abspath('./'), path)
        except Exception as e:
            # print('qui',e)
            raise APIerror('problem with local file delivery: %s' %
                           e, status_code=410)


@ns_conf.route('/js9/<path:path>', methods=['GET', 'POST'])
# @app.route('/js9/<path:path>',methods=['GET','POST'])
class JS9(Resource):
    @api.doc(responses={410: 'problem with  js9 library'}, params={'path': 'the file path for the JS9 library'})
    def get(self, path):
        """
        serves the js9 library
        """
        try:
            return send_from_directory(os.path.abspath('static/js9/'), path)
        except Exception as e:
            # print('qui',e)
            raise APIerror('problem with local file delivery: %s' %
                           e, status_code=410)


@ns_conf.route('/get_js9_plot')
class GetJS9Plot(Resource):
    @api.doc(responses={410: 'problem with js9 image generation'}, params={'file_path': 'the file path', 'ext_id': 'extension id'})
    def get(self):
        """
        returns the js9 image display
        """
        api_parser = reqparse.RequestParser()
        api_parser.add_argument(
            'file_path', required=True, help="the name of the file", type=str)
        api_parser.add_argument('ext_id', required=False,
                                help="extension id", type=int, default=4)
        api_args = api_parser.parse_args()
        file_path = api_args['file_path']
        ext_id = api_args['ext_id']

        try:
            tmp_file = FitsFile(file_path)
            tmp_file.file_path._set_file_path(
                tmp_file.file_path.dir_name, 'js9.fits')

            data = FitsFile(file_path).open()[ext_id]
            print('==>', tmp_file.file_path, ext_id)
            data.writeto(tmp_file.file_path.path, overwrite=True)
        except Exception as e:
            # print('qui',e)
            raise APIerror('problem with input file: %s' % e, status_code=410)

        region_file = None
        if 'region_file' in api_args.keys():
            region_file = api_args['region_file']
        print('file_path,region_file', tmp_file.file_path.path, region_file)
        try:
            img = Image(None, None)
            #print('get_js9_plot path',tmp_file.file_path.path)
            img = img.get_js9_html(
                tmp_file.file_path.path, region_file=region_file)

        except Exception as e:
            # print('qui',e)
            raise APIerror('problem with js9 image generation: %s' %
                           e, status_code=410)

        return output_html(img, 200)


@ns_conf.route('/test_js9')
class TestJS9Plot(Resource):
    """
    tests js9 with a predefined file
    """
    @api.doc(responses={410: 'problem with js9 image generation'})
    def get(self):
        try:
            img = Image(None, None)
            #print('get_js9_plot path',file_path)
            img = img.get_js9_html('dummy_prods/isgri_query_mosaic.fits')

        except Exception as e:
            # print('qui',e)
            raise APIerror('problem with js9 image generation: %s' %
                           e, status_code=410)

        return output_html(img, 200)


# @app.route('/get_js9_plot', methods=['POST', 'GET'])
# def js9_plot():
#    args = request.args.to_dict()
#    file_path = args['file_path']
#    region_file=None
#    if 'region_file' in args.keys():
#        region_file= args['region_file']
#    print('file_path,region_file',file_path,region_file)
#    img=Image(None,None)
#    #print('get_js9_plot path',file_path)
#    return img.get_js9_html(file_path,region_file=region_file)

# @app.route('/test_js9', methods=['POST', 'GET'])
# def test_js9():
#    img = Image(None,None)
#    # print('get_js9_plot path',file_path)
#    return img.get_js9_html('dummy_prods/isgri_query_mosaic.fits')

def conf_app(conf):
    app.config['conf'] = conf
    if conf.sentry_url is not None:
        sentry = Sentry(app, dsn=conf.sentry_url)
        logger.warning("sentry not used")
    return app

def run_app(conf, debug=False, threaded=False):
    conf_app(conf)
    app.run(host=conf.bind_host, port=conf.bind_port,
            debug=debug, threaded=threaded)


if __name__ == "__main__":
    app.run()
