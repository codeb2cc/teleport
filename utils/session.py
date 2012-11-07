# -*- coding:utf-8 -*-

# Last Change: 2012-11-08 05:24

from bson.objectid import ObjectId
from bson.errors import InvalidId

from werkzeug.contrib.sessions import SessionStore

from ..db import db

class MongoSessionStore(SessionStore):
    def __init__(self, session_class=None, collection=None):
        SessionStore.__init__(self, session_class)

        if not collection:
            raise ValueError('collection can not be None')

        self.collection = db[collection]

        # Empty session collection
        self.collection.remove()

    def save(self, session):
        _data = dict(session)
        _data['sid'] = session.sid

        _id = self.collection.insert(_data)

    def delete(self, session):
        _error = self.collection.remove({ 'sid': session.sid }, safe=True)

    def get(self, sid):
        _doc = self.collection.find_one({ 'sid': sid })

        if _doc:
            return self.session_class(_doc, sid, False)

        return None
