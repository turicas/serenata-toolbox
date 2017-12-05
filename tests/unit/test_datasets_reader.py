import io
import textwrap
from collections import OrderedDict
from unittest import TestCase

from serenata_toolbox.datasets import read_schema

import rows


class ReaderTestCase(TestCase):

    def test_read_schema(self):
        csv_data = textwrap.dedent('''
        field_name,field_type
        f1,text
        f2,integer
        f3,json
        ''').strip()

        result = read_schema(io.StringIO(csv_data))
        expected = OrderedDict([
            ('f1', rows.fields.TextField),
            ('f2', rows.fields.IntegerField),
            ('f3', rows.fields.JSONField)
        ])

        assert result == expected
