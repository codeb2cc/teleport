# -*- coding:utf-8 -*-

import logging


def create_logger():
    formatter = logging.Formatter("%(levelname)s %(asctime)s [%(module)s]%(funcName)s|%(lineno)d: %(message)s", "%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger = logging.getLogger()

    logger.addHandler(console_handler)

    return logger

logger = create_logger()
