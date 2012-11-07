# -*- coding:utf-8 -*-

# Last Change: 2012-11-08 04:38

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

    def save(self, session):
        _id = self.collection.insert(dict(session))

    def delete(self, session):
        _error = self.collection.remove({ 'sid': session.sid })

    def get(self, sid):
        _doc = self.collection.find_one({ 'sid': sid })

        return self.session_class(_doc, sid, False)
