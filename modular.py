#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask
from lib.check_auth import check_auth
PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(__file__))
)

FLASK_JSONRPC_PROJECT_DIR = os.path.join(PROJECT_DIR, os.pardir)
if os.path.exists(FLASK_JSONRPC_PROJECT_DIR) \
        and not FLASK_JSONRPC_PROJECT_DIR in sys.path:
    sys.path.append(FLASK_JSONRPC_PROJECT_DIR)

from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@jsonrpc.method('App.index',authenticated=check_auth)
def index(name):
    return u'Welcome to Flask JSON-RPC ss %s'%(name)


import api.search
import api.indexKey

if __name__ == '__main__':
    app.run(host="0.0.0.0")
