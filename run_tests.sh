#!/bin/sh -e

cd "`dirname $0`"/testproject
./manage.py test
