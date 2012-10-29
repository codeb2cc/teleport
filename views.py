# -*- coding:utf-8 -*-

# Last Change: 2012-10-29 23:18

import json, datetime
import traceback

import pymongo

from bson.objectid import ObjectId
from bson.errors import InvalidId

from bottle import get, post, put, delete
from bottle import view, request, response, abort

from .db import db
from .tools.paginator import Paginator
from .tools.hash_tool import str2md5

@get('/')
@view('index.tpl')
def index():
    try:
        tpl_dict = {}

        return tpl_dict
    except Exception as e:
        abort(500)

@post('/sigin/')
def sigin():
    pass

@post('/login/')
def login():
    pass

@post('/logout/')
def logout():
    pass

@get('/ping')
def ping():
    try:
        token = request.query.get('token', type=string)
    except Exception as e:
        abort(500)

@get('/get/')
def get():
    pass

@put('/put/')
def add():
    pass

@delete('/delete/')
def delete():
    pass

