# -*- coding:utf-8 -*-

# Last Change: 2012-11-02 01:11

import json, datetime
import random
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

def _gate_parser(doc):
    try:
        res = {
                    'id': str(doc['_id']),
                    'label': doc['label'],
                    'description': doc['description'],
                    'token': doc['token'],
                    'records': doc['records'],
                    'counter': doc['counter'],
                    'date': str(doc['date']),
                }

        return res
    except Exception as e:
        traceback.print_exc()
        return None

@get('/get/')
def get():
    try:
        _id = request.query.get('id')

        if _id:
            gate = db['teleport.gate'].find_one(ObjectId(_id))
            res = _gate_parser(gate)
        else:
            cursor = db['teleport.gate'].find(
                    sort = [ ('date', pymongo.DESCENDING), ],
                )
            res = [ _gate_parser(doc) for doc in cursor ]

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'data': res })
    except InvalidId as e:
        abort(400)
    except Exception as e:
        traceback.print_exc()
        abort(500)


_SYSR = random.SystemRandom()
_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def _random_token(length=32):
    return ''.join(_SYSR.choice(_CHARS) for i in xrange(length))

@post('/post/')
def post():
    try:
        _label = request.forms['label']
        _description = request.forms.get('description')

        gate = {
                'label': _label,
                'description': _description,
                'token': _random_token(),
                'records': ['0.0.0.0', ],
                'counter': 0,
                'user_id': None,
                'date': datetime.datetime.now(),
            }

        _id = db['teleport.gate'].insert(gate)

        # Reload
        gate = db['teleport.gate'].find_one(ObjectId(_id))

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'data': _gate_parser(gate) })
    except KeyError as e:
        abort(400)
    except Exception as e:
        traceback.print_exc()
        abort(500)

@put('/put/')
def put():
    try:
        _id = request.forms['id']

        _label = request.forms.get('label')
        _description = request.forms.get('description')

        gate = db['teleport.gate'].find_one(ObjectId(_id))

        if _label: gate['label'] = _label
        if _description: gate['description'] = _description

        _id = db['teleport.gate'].save(gate, safe=True)

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'id': str(_id) })
    except InvalidId as e:
        abort(400)
    except pymongo.errors.OperationFailure as e:
        abort(400)
    except Exception as e:
        traceback.print_exc()
        abort(500)

@delete('/delete/')
def delete():
    try:
        _id = request.forms['id']

        err = db['teleport.gate'].remove(ObjectId(_id), safe=True)

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK' })
    except InvalidId as e:
        abort(400)
    except KeyError as e:
        abort(400)
    except Exception as e:
        traceback.print_exc()
        abort(500)

