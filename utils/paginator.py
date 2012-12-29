# -*- coding:utf-8 -*-

import math
import pymongo

class Paginator(object):
    def __init__(self, cursor, PER_PAGE=10):
        if not isinstance(cursor, pymongo.cursor.Cursor):
            raise TypeError('cursor must be an instance of Cursor')

        self._cursor = cursor
        self._limit = PER_PAGE

    def __getitem__(self, index):
        if not isinstance(index, (int, long)):
            raise TypeError('index must be an instance of int/long')

        if index < 0 or index >= self.length:
            raise IndexError

        skip = index * self._limit
        limit = skip + self._limit
        return self._cursor[skip:limit]

    @property
    def count(self):
        return self._cursor.count()

    @property
    def length(self):
        return int(math.ceil(self.count / float(self._limit)))

