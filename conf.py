# -*- coding:utf-8 -*-

# Last Change: 2012-11-08 03:23

DEBUG = True

DB = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'USER': 'saber',
        'PASSWORD': '',
        'NAME': 'teleport',
    }

TEMPLATE_PATH = [
        './templates/',
    ]

LABEL_MAX = 48
MESSAGE_MAX = 1024

HMAC_METHOD = 'sha1'
HMAC_SALT_LEN = 8
HMAC_PASSWORD_LEN = 40
