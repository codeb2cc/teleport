# -*- coding:utf-8 -*-

import hashlib

def str2md5(io, hexadecimal=True):
    try:
        md5 = hashlib.md5()
        md5.update(io)

        return hexadecimal and md5.hexdigest() or md5.digest()
    except Exception as e:
        raise e
