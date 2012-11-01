# -*- coding:utf-8 -*-

# Last Change: 2012-10-30 17:13

from pymongo import Connection
from pymongo.errors import AutoReconnect

from .conf import DB

try:
    conn = Connection(
            host = DB['HOST'],
            port = DB['PORT'],
        )

    db = conn[DB['NAME']]
    # db.authenticate(DB['USER'], DB['PASSWORD'])
except AutoReconnect as e:
    print '[WARNING] Connect to MongDB failed.'
    db = None
except Exception as e:
    raise e

# Model Definition
# user = {
        # 'username': '',
        # 'email': '',
        # 'password': '',
    # }

# gate = {
        # 'label': '',
        # 'description': '',
        # 'token': '',
        # 'records': [
                # { 'ip': '', 'date': '' }
            # ],
        # 'counter': 0,
        # 'user_id': '',
        # 'date': '',
    # }
