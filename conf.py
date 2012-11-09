# -*- coding:utf-8 -*-

# Last Change: 2012-11-09 11:47

DEBUG = True

DB = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'USER': 'saber',
        'PASSWORD': '',
        'NAME': 'teleport',
    }

SESSION_COLLECTION = 'session'

TEMPLATE_PATH = [
        './templates/',
    ]

LABEL_MAX = 48
MESSAGE_MAX = 1024

HMAC_METHOD = 'sha1'
HMAC_SALT_LEN = 8
HMAC_PASSWORD_LEN = 40
