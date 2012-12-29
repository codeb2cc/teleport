# -*- coding:utf-8 -*-

# Last Change: 2012-12-29 20:56

import os
import bottle

from teleport.conf import TEMPLATE_PATH
from teleport.views import *

bottle.TEMPLATE_PATH = []
for path in TEMPLATE_PATH:
    bottle.TEMPLATE_PATH.append(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        )

app = bottle.default_app()
