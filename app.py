#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-

import argparse 
import logging
import os

import flask
from flask import Flask

import flask_bootstrap
import flask_cas

app = Flask(__name__)
flask_bootstrap.Bootstrap(app)
cas = flask_cas.CAS(app)
app.logger.addHandler(logging.StreamHandler())
app.secret_key = os.environ.get('SECRET_KEY', None)
app.config['CAS_SERVER'] = os.environ.get('CAS_SERVER', None)
app.config['CAS_AFTER_LOGIN'] = 'route_root'

@app.route('/')
def route_root():
    return flask.render_template(
        'layout.html',
        username = cas.username,
    )

def create_parser():

    parser = argparse.ArgumentParser(
        description="", 
    )
    parser.add_argument(
       "--host", "-H",
       type=str,
       default=None,
    )
    parser.add_argument(
       "--port", "-P",
       type=int,
       default=None,
    )
    parser.add_argument(
       "--debug", "-D",
       type=bool,
       default=False,
    )
    parser.add_argument(
       "--cas_server", "-c",
       type=str,
       required=True,
    )
    parser.add_argument(
        "--secret_key", "-S",
        type=str,
        default="DEFAULT SECRET KEY",
    )
    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    app.secret_key = args.secret_key
    app.config['CAS_SERVER'] = args.cas_server
    app.run(
        host=args.host, 
        port=args.port,
        debug=args.debug,
    )
