#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django_dumpdb


def get_long_description():
    return open('README').read()

setup(
    name='django-dumpdb',
    version=django_dumpdb.__version__,
    description='Django dumpdb/restoredb management commands',
    long_description=get_long_description(),
    author='Andrey Golovizin',
    author_email='golovizin@gmail.com',
    url='http://code.google.com/p/django-dumpdb/',
    packages=['django_dumpdb'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Topic :: Utilities',
    ],
)
