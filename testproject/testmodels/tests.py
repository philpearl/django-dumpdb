"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from os import path
from io import BytesIO

from django.test import TestCase
from django.core import serializers
from django.core.management.commands import dumpdata

from django_dumpdb import dumprestore

DATA_PATH = path.join(path.dirname(__file__), 'testdata')
print DATA_PATH


class TestDumpRestore(TestCase):
    data_set = 'empty'

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
            self.assertEqual(output.getvalue(), reference_dump.read())

    def test_restore(self):
        with self.open_dump() as dump:
            dumprestore.load(dump)

        result = dumpdata.Command().handle(format='json', indent=4) + '\n'
        with self.open_fixture() as reference_fixture:
            self.assertEqual(result, reference_fixture.read())
