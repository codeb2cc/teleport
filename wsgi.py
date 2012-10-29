# -*- coding:utf-8 -*-

# Last Change: 2012-10-29 21:49

import os
import bottle

from .conf import TEMPLATE_PATH
from .views import *

bottle.TEMPLATE_PATH = []
for path in TEMPLATE_PATH:
    bottle.TEMPLATE_PATH.append(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        )

app = bottle.default_app()
