"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from os import path
from io import BytesIO
from difflib import unified_diff

from django.test import TestCase
from django.core import serializers
from django.core.management.commands import dumpdata

from django_dumpdb import dumprestore

DATA_PATH = path.join(path.dirname(__file__), 'testdata')
print DATA_PATH


class TestDumpRestoreBase(object):
    data_set = None

    def open_fixture(self):
        return open(path.join(DATA_PATH, self.data_set, 'dump.json'))

    def open_dump(self):
        return open(path.join(DATA_PATH, self.data_set, 'dump'))

    def test_dump(self):
        """Dump test data and compare with the reference file."""

        with self.open_fixture() as fixture:
            objects = serializers.deserialize('json', fixture)
            for obj in objects:
                obj.save()

        output = BytesIO(encoding=None)
        dumprestore.dump(file=output)
        with self.open_dump() as reference_dump:
            self.assertTextEqual(reference_dump.read(), output.getvalue())

    def test_restore(self):
        with self.open_dump() as dump:
            dumprestore.load(dump)

        result = dumpdata.Command().handle(format='json', indent=4) + '\n'
        with self.open_fixture() as reference_fixture:
            self.assertTextEqual(reference_fixture.read(), result)

    def assertTextEqual(self, expected, got):
        self.assertEqual(
            got,
            expected,
            '\n' + '\n'.join(unified_diff(expected.splitlines(), got.splitlines(), 'expected', 'got')),
        )

def make_tests():
    with open(path.join(DATA_PATH, 'index')) as index:
        data_sets = [line.strip() for line in index]

    for data_set in data_sets:
        print 'Data set', data_set
        cls_name = 'TestDumpRestore_%s' % data_set
        globals()[cls_name] = type(cls_name, (TestDumpRestoreBase, TestCase), {'data_set': data_set})

 
make_tests()
