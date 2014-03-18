SQLFormatter: Beautiful colored SQL staments for logging
========================================================

Logging your SQL to the console helps you understand whats going on under the ORM.

However, queries can get pretty big resulting on a code wall.

*SQLFormater* is a logging formatter that *idents* and *colorize* your SQL statements making everything legible again.

.. image:: https://pypip.in/v/sqlformatter/badge.png
    :target: https://crate.io/packages/sqlformatter/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/sqlformatter/badge.png
    :target: https://crate.io/packages/sqlformatter/
    :alt: Number of PyPI downloads


Install
-------

.. code-block:: console

    pip install sqlformatter

Usage
-----

If you're using Django, simply add it to your LOGGING settings:

   .. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'sqlhandler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'sqlformatter'
            }
        },
        'formatters': {
            'sqlformatter': {
                '()': 'sqlformatter.SqlFormatter',
                'format': '%(levelname)s %(message)s',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['sqlhandler'],
                'level': 'DEBUG',
            },
        }
    }


License
=======

The MIT License (MIT)

Copyright (c) 2013 Henrique Bastos <henrique at bastos dot net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
