# -*- coding:utf-8 -*-

# Last Change: 2012-11-08 07:02

import json, datetime
import random
import sha
import traceback

import pymongo

from bson.objectid import ObjectId
from bson.errors import InvalidId

from bottle import get, post, put, delete
from bottle import template
from bottle import view, request, response, abort
from bottle import HTTPError

from werkzeug.security import safe_str_cmp, safe_join
from werkzeug.security import gen_salt, generate_password_hash, check_password_hash

from .db import db
from .conf import DEBUG
from .conf import LABEL_MAX, MESSAGE_MAX
from .conf import HMAC_METHOD, HMAC_SALT_LEN, HMAC_PASSWORD_LEN
from .conf import SESSION_COLLECTION
from .utils.session import MongoSessionStore
from .utils.paginator import Paginator
from .utils.hash_tool import str2md5
from .utils.validator import validate_email

session_store = MongoSessionStore(collection=SESSION_COLLECTION)

@get('/panel/')
@view('panel.tpl')
def panel():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            response.status = 302
            response.set_header('Location', '/')
            return
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        tpl_dict = {
            'user': user,
            'debug': DEBUG,
        }

        return tpl_dict
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@get('/')
@view('auth.tpl')
def auth():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        if _session_id and session_store.get(_session_id):
            response.status = 302
            response.set_header('Location', '/panel/')
            return
        # }

        tpl_dict = { 'debug': DEBUG }

        return tpl_dict
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@post('/signin/')
def signin():
    try:
        _salt = request.forms['key']
        _email = request.forms['email']
        _password = request.forms['password']
        _raw = request.forms['raw']

        if len(_salt) != HMAC_SALT_LEN or len(_password) != HMAC_PASSWORD_LEN or len(_raw) != HMAC_PASSWORD_LEN:
            abort(400)

        user = db['teleport.user'].find_one({ 'email': _email })

        if not user:
            return template('passport', debug=DEBUG, title='Login Failed', message='Invalid Email or Password' )

        method, salt, hashval = user['password'].split('$', 2)

        if not safe_str_cmp(_raw, hashval):
            return template('passport', debug=DEBUG, title='Login Failed', message='Invalid Email or Password' )

        user['password'] = '%s$%s$%s' % (HMAC_METHOD, _salt, _password)

        _id = db['teleport.user'].save(user, safe=True)

        _session = session_store.new()
        _session['uid'] = str(_id)
        session_store.save(_session)

        response.status = 302
        response.set_header('Location', '/panel/')
        response.set_cookie('_session', _session.sid, path='/')
        return
    except KeyError as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@get('/signout/')
def signout():
    try:
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if session:
            session_store.delete(session)

        response.status = 302
        response.set_header('Location', '/')
        response.delete_cookie('_session', path='/')
        return
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@post('/signup/')
def signup():
    try:
        _salt = request.forms['key']
        _email = request.forms['email']
        _password = request.forms['password']

        if len(_salt) != HMAC_SALT_LEN or len(_password) != HMAC_PASSWORD_LEN:
            abort(400)

        user = {
            'email': _email,
            'password': '%s$%s$%s' % (HMAC_METHOD, _salt, _password),
            'date'   : datetime.datetime.utcnow(),
        }

        _id = db['teleport.user'].insert(user)

        _session = session_store.new()
        _session['uid'] = str(_id)
        session_store.save(_session)

        response.status = 302
        response.set_header('Location', '/panel/')
        response.set_cookie('_session', _session.sid, path='/')
    except KeyError as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@get('/challenge/')
def challenge():
    try:
        _id = request.query.get('id', type=str)

        if not _id or not validate_email(_id):
            abort(400)

        user = db['teleport.user'].find_one({ 'email': _id })

        if not user:
            _salt = ''
        else:
            method, _salt, hashval = user['password'].split('$', 2)

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'code': [_salt, gen_salt(HMAC_SALT_LEN)] })
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@get('/ping/')
def api_ping():
    try:
        _token = request.query.get('token', type=str)
        _ip = request.query.get('ip', type=str) or request.remote_addr
        _message = request.query.get('message', type=str, default='')

        gate = db['teleport.gate'].find_one({ 'token': _token })

        if not gate:
            abort(400)

        gate['counter'] += 1
        len(gate['records']) >= 5 and gate['records'].pop()
        gate['records'].insert(0, {
                'ip'     : _ip,
                'message': _message[:MESSAGE_MAX],
                'date'   : datetime.datetime.utcnow()
            })

        _id = db['teleport.gate'].save(gate, safe=True)

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'ip': _ip })
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

def _gate_parser(doc):
    try:
        res = {
                    'id'         : str(doc['_id']),
                    'label'      : doc['label'],
                    'token'      : doc['token'],
                    'records'    : doc['records'],
                    'counter'    : doc['counter'],
                    'date'       : doc['date'].isoformat(),
                }

        for record in res['records']:
            record['date'] = record['date'].isoformat()

        return res
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        return None

@get('/get/')
def api_fetch():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            abort(400)
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        _id = request.query.get('id')

        if _id:
            gate = db['teleport.gate'].find_one({ 'id': ObjectId(_id), 'user': user['_id'] })
            res = _gate_parser(gate)
        else:
            cursor = db['teleport.gate'].find({ 'user': user['_id'] },
                    sort = [ ('date', pymongo.DESCENDING), ],
                )
            res = [ _gate_parser(doc) for doc in cursor ]

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'data': res })
    except InvalidId as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)


_SYSR = random.SystemRandom()
_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def _random_token(length=32):
    return ''.join(_SYSR.choice(_CHARS) for i in xrange(length))

@post('/post/')
def api_add():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            abort(400)
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        _label = request.forms['label']

        print user

        gate = {
                'label': _label[:LABEL_MAX],
                'token': _random_token(),
                'records': [],
                'counter': 0,
                'user': user['_id'],
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
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@put('/put/')
def api_update():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            abort(400)
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        _id = request.forms['id']
        _label = request.forms['label']

        gate = db['teleport.gate'].find_one({ 'id': ObjectId(_id), 'user': user['_id'] })

        gate['label'] = _label[:LABEL_MAX]
        db['teleport.gate'].save(gate, safe=True)

        # Reload
        gate = db['teleport.gate'].find_one(ObjectId(_id))

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'data': _gate_parser(gate) })
    except InvalidId as e:
        abort(400)
    except pymongo.errors.OperationFailure as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@post('/reset/')
def api_reset():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            abort(400)
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        _id = request.forms['id']

        gate = db['teleport.gate'].find_one({ 'id': ObjectId(_id), 'user': user['_id'] })

        gate['token'] =  _random_token()
        db['teleport.gate'].save(gate, safe=True)

        # Reload
        gate = db['teleport.gate'].find_one(ObjectId(_id))

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK', 'data': _gate_parser(gate) })
    except InvalidId as e:
        abort(400)
    except pymongo.errors.OperationFailure as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

@delete('/delete/')
def api_delete():
    try:
        # Session {
        _session_id = request.get_cookie('_session')

        session = session_store.get(_session_id)
        if not session:
            abort(400)
        # }

        user = db['teleport.user'].find_one(ObjectId(session['uid']))

        _id = request.forms['id']

        err = db['teleport.gate'].remove({ 'id': ObjectId(_id), 'user': user['_id'] }, safe=True)

        response.content_type = 'application/json'
        response.set_header('Cache-Control', 'no-cache')
        return json.dumps({ 'status': 'OK' })
    except InvalidId as e:
        abort(400)
    except KeyError as e:
        abort(400)
    except HTTPError as e:
        raise e
    except Exception as e:
        traceback.print_exc()
        abort(500)

