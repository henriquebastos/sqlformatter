# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.rst')
REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')

setup(name='sqlformatter',
      version='1.2',
      description='SQLFormatter: Beautiful colored SQL staments for logging',
      long_description=open(README).read(),
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      py_modules=['sqlformatter'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      install_requires=open(REQUIREMENTS).readlines(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/henriquebastos/sqlformatter/',)
