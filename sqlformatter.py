# coding: utf-8
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

        msg = record.msg

        if self.parse:
            msg = sqlparse.format(record.msg, reindent=self.reindent, keyword_case=self.keyword_case)

        if self.highlight:
            msg = highlight(msg, self._lexer, self._formatter)

        return msg


class LogDb:
    def __init__(self):
        self.handler = None
        self.propagate = None

    def __call__(self, **options):
        logger = logging.getLogger('django.db.backends')

        if self.handler is None:
            # Enable
            self.handler = logging.StreamHandler(sys.stdout)
            self.handler.setFormatter(SqlFormatter(**options))
            logger.addHandler(self.handler)
            logger.setLevel(logging.DEBUG)

            self.propagate = logger.propagate
            logger.propagate = False
        else:
            # Disable
            logger.removeHandler(self.handler)
            self.handler = None
            logger.setLevel(logging.NOTSET)

            logger.propagate = self.propagate
            self.propagate = None

        return self.handler

logdb = LogDb()
