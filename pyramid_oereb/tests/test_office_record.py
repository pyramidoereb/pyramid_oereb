# -*- coding: utf-8 -*-

__author__ = 'François Voisard'
__create_date__ = '27.03.2017'

import pytest

from pyramid_oereb.lib.records.office import OfficeRecord


def test_get_fields():
    expected_fields = [
            'name',
            'uid',
            'office_at_web',
            'line1',
            'line2',
            'street',
            'number',
            'postal_code',
            'city'
    ]
    fields = OfficeRecord.get_fields()
    assert fields == expected_fields


def test_mandatory_fields():
    with pytest.raises(TypeError):
        OfficeRecord()


def test_init():
    record = OfficeRecord(name='a', uid='ch99', postal_code=4123)
    assert record.name == 'a'
    assert record.line1 is None
    assert isinstance(record.postal_code, int)
