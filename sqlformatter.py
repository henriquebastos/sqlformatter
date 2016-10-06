# coding: utf-8
import os
import sys
import logging
import sqlparse
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import Terminal256Formatter


class SqlFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        self.highlight = kwargs.pop('highlight', True)
        self.style = kwargs.pop('style', 'default')

        self.parse = kwargs.pop('parse', True)
        self.reindent = kwargs.pop('reindent', True)
        self.keyword_case = kwargs.pop('keyword_case', 'upper')

        self._lexer = SqlLexer()
        self._formatter = Terminal256Formatter(style=self.style)

        super(SqlFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        super(SqlFormatter, self).format(record)

        msg = record.sql

        if self.parse:
            msg = sqlparse.format(msg, reindent=self.reindent, keyword_case=self.keyword_case)

        if self.highlight:
            msg = highlight(msg, self._lexer, self._formatter)

        return msg


class LogDb:
    def __init__(self, name='django.db.backends', handler=None, propagate=None, **kwargs):
        self.name = name
        self.propagate = propagate

        self.handler = handler or logging.StreamHandler(sys.stdout)
        self.formatter = SqlFormatter(**kwargs)

        self.running = False

    def __call__(self, **options):
        # Toggle
        if not self.running:
            self.enable()
            self.running = True
        else:
            self.disable()
            self.running = False

        return self.running

    def enable(self):
        logger = logging.getLogger(self.name)

        self.handler.setFormatter(self.formatter)
        logger.addHandler(self.handler)
        logger.setLevel(logging.DEBUG)

        self.propagate = logger.propagate
        logger.propagate = False

    def disable(self):
        logger = logging.getLogger(self.name)

        logger.removeHandler(self.handler)
        logger.setLevel(logging.NOTSET)

        logger.propagate = self.propagate
        self.propagate = None

if os.name == 'nt':
    logdb = LogDb(highlight=False)
else:
    logdb = LogDb()
