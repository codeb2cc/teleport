# -*- coding:utf-8 -*-

import datetime
import traceback

from gevent.server import DatagramServer

from teleport.db import db
from teleport.conf import MESSAGE_MAX
from teleport.utils.logger import logger


class PingServer(DatagramServer):
    def handle(self, data, address):
        try:
            _raw = data.split('\t')

            _token = _raw[0]
            _ip = address[0]
            _lng = float(_raw[1])
            _lat = float(_raw[2])
            _message = _raw[3]

            gate = db['gate'].find_one({ 'token': _token })

            if not gate:
                self.socket.sendto('Error', address)
                return False

            gate['counter'] += 1
            len(gate['records']) >= 5 and gate['records'].pop()
            gate['records'].insert(0, {
                    'ip'     : _ip,
                    'lng'    : _lng,
                    'lat'    : _lat,
                    'message': _message[:MESSAGE_MAX],
                    'date'   : datetime.datetime.utcnow()
                })

            _id = db['gate'].save(gate, safe=True)


            self.socket.sendto('OK', address)
        except Exception:
            traceback.print_exc()
            self.socket.sendto('Error', address)


def run_server(port):
    try:
        PingServer(':%d' % port).serve_forever()
    except Exception:
        traceback.print_exc()

