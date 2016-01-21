SQLFormatter: Beautiful colored SQL statements for logging
==========================================================

Logging your SQL to the console helps you understand whats going on under the ORM.

However, queries can get pretty big resulting on a code wall.

*SQLFormater* is a logging formatter that *idents* and *colorize* your SQL statements making everything legible again.

.. image:: https://img.shields.io/pypi/v/sqlformatter.svg
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/sqlformatter.svg
    :alt: Number of PyPI downloads


How it looks like?
------------------

.. image:: https://raw.githubusercontent.com/henriquebastos/sqlformatter/master/screenshot.png
    :alt: Screenshot


Install
-------

.. code-block:: console

    pip install sqlformatter

Usage
-----

There are 2 ways of using it.

Temporarily enable it during a console session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During a console session it maybe interesting to show your queries while experimenting.

You can toggle sql output logging by calling the helper function `logdb`.

.. code-block:: python

    from sqlformatter import logdb
    # Enable
    logdb()
    
    # Run your query
    MyModel.objects.all() 
    
    # Disable
    logdb()

Add it to your Django Logging settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add it to yout Django LOGGING settings:

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

Customization
-------------

You can passa many options to customize `SqlFormatter` either instantiating it 
directly or calling the `logdb` helper.

Check out the source code.

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
