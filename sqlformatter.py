# coding: utf-8
import logging
import sqlparse
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import TerminalFormatter


LEXER = SqlLexer()
FORMATTER = TerminalFormatter()

class SqlFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super(SqlFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        msg = super(SqlFormatter, self).format(record)
        msg = sqlparse.format(record.msg, reindent=True, keyword_case='upper')
        return highlight(msg, LEXER, FORMATTER)
