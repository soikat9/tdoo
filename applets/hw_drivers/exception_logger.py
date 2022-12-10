# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import logging
import sys


class ExceptionLogger:
    """
    Redirect Exceptions to the logger to keep track of them in the log file.
    """

    def __init__(self):
        self.logger = logging.getLogger()

    def write(self, message):
        if message != '\n':
            self.logger.error(message)

    def flush(self):
        pass

sys.stderr = ExceptionLogger()
