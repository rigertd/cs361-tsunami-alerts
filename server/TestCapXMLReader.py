#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the CapXMLReader module.
"""
from CapXMLReader import CapXMLReader
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import raises
from datetime import datetime
from dateutil import tz
#================================================
# Initialization Unit Tests
#================================================
def test_init_happy_path():
    parser = CapXMLReader()
    assert_not_equal(parser, None)

@raises(TypeError)
def test_init_extra_arg():
    parser = CapXMLReader('foo')
    assert_equal(parser, None)

def test_reset_happy_path():
    parser = CapXMLReader()
    parser.add_by_lat_long(0.0, 0.0)
    assert_equal(len(parser.data['locations']), 1)
    parser.reset()
    assert_equal(len(parser.data['locations']), 0)

#================================================
# get_alert_data Unit Tests
#================================================
class Test_get_alert_data(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def setUp(self):
        """
        Run before each test method is run
        """
        self.parser.reset()

    def test_happy_path(self):
        self.parser.data['id'] = 'test'
        assert_true(self.parser.add_by_lat_long(44.564089096, -123.28061099))
        assert_equal(self.parser.get_alert_data(), self.parser.data)

    def test_no_data(self):
        assert_equal(self.parser.get_alert_data(), None)

#================================================
# add_by_lat_long Unit Tests
#================================================
class Test_add_by_lat_long(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def setUp(self):
        """
        Run before each test method is run
        """
        self.parser.reset()

    def test_floats_happy_path(self):
        assert_true(self.parser.add_by_lat_long(44.564089096, -123.28061099))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 44.564089096)
        assert_almost_equal(self.parser.data['locations'][0][1], -123.28061099)

    def test_floats_max_values(self):
        assert_true(self.parser.add_by_lat_long(90.0, 180.0))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 90.0)
        assert_almost_equal(self.parser.data['locations'][0][1], 180.0)

    def test_floats_min_values(self):
        assert_true(self.parser.add_by_lat_long(-90.0, -180.0))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], -90.0)
        assert_almost_equal(self.parser.data['locations'][0][1], -180.0)

    def test_floats_lat_too_high(self):
        assert_false(self.parser.add_by_lat_long(90.1, 0.0))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_floats_lat_too_low(self):
        assert_false(self.parser.add_by_lat_long(-90.1, 0.0))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_floats_long_too_high(self):
        assert_false(self.parser.add_by_lat_long(0.0, 180.1))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_floats_long_too_low(self):
        assert_false(self.parser.add_by_lat_long(0.0, -180.1))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_strings_happy_path(self):
        assert_true(self.parser.add_by_lat_long('44.564089096', '-123.28061099'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 44.564089096)
        assert_almost_equal(self.parser.data['locations'][0][1], -123.28061099)

    def test_strings_max_values(self):
        assert_true(self.parser.add_by_lat_long('90.0', '180.0'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 90.0)
        assert_almost_equal(self.parser.data['locations'][0][1], 180.0)

    def test_strings_min_values(self):
        assert_true(self.parser.add_by_lat_long('-90.0', '-180.0'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], -90.0)
        assert_almost_equal(self.parser.data['locations'][0][1], -180.0)

    def test_strings_lat_too_high(self):
        assert_false(self.parser.add_by_lat_long('90.1', '0.0'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_strings_lat_too_low(self):
        assert_false(self.parser.add_by_lat_long('-90.1', '0.0'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_strings_long_too_high(self):
        assert_false(self.parser.add_by_lat_long('0.0', '180.1'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_strings_long_too_low(self):
        assert_false(self.parser.add_by_lat_long('0.0', '-180.1'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_non_numeric_lat(self):
        assert_false(self.parser.add_by_lat_long('asdf', '0.0'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_non_numeric_long(self):
        assert_false(self.parser.add_by_lat_long('0.0', 'asdf'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

    def test_non_numeric_both(self):
        assert_false(self.parser.add_by_lat_long('asdf', 'asdf'))
        assert_equal(len(self.parser.data['locations']), 0) # zero items

#================================================
# add_by_address Unit Tests
#================================================
class Test_add_by_address(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def setUp(self):
        """
        Run before each test method is run
        """
        self.parser.reset()

    def test_city_state_zip_happy_path(self):
        assert_true(self.parser.add_by_address('Corvallis, OR 97331'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 44.564089096)
        assert_almost_equal(self.parser.data['locations'][0][1], -123.28061099)

    def test_full_address_happy_path(self):
        assert_true(self.parser.add_by_address('500 SW Jefferson Way, Corvallis, OR 97331'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 44.5646016)
        assert_almost_equal(self.parser.data['locations'][0][1], -123.27254)

    def test_invalid_address(self):
        assert_false(self.parser.add_by_address('adskfjs;ldkjf;lkasjdf'))
        assert_equal(len(self.parser.data['locations']), 0) # Should be empty

    def test_incorrect_zip(self):
        assert_false(self.parser.add_by_address('Corvallis, OR 98108'))
        assert_equal(len(self.parser.data['locations']), 0) # Should be empty

    def test_lat_long_string(self):
        assert_true(self.parser.add_by_address('44.564089096,-123.28061099'))
        assert_equal(len(self.parser.data['locations']), 1) # one item
        assert_almost_equal(self.parser.data['locations'][0][0], 44.564089096, places=3)
        assert_almost_equal(self.parser.data['locations'][0][1], -123.28061099, places=3)

#================================================
# parse Unit Tests
#================================================
class Test_parse_real_alert(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()
        f = open(r'testdata/actual.xml', 'r')
        data = f.read()
        f.close()
        self.parser.parse(data)

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def test_onsetDate(self):
        assert_equal(self.parser.data['onsetDate'], datetime(2012, 10, 28, 3, 7, 27, tzinfo=tz.tzutc()))

    def test_expireDate(self):
        assert_equal(self.parser.data['expireDate'], datetime(2012, 10, 28, 5, 7, 27, tzinfo=tz.tzutc()))

    def test_isUpdate_false(self):
        assert_false(self.parser.data['isUpdate'])

    def test_cancel_flag(self):
        assert_false(self.parser.data['isCancel'])

    def test_id(self):
        assert_equal(self.parser.data['id'], 'mcl1uw')

class Test_parse_real_update(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()
        f = open(r'testdata/update.xml', 'r')
        data = f.read()
        f.close()
        self.parser.parse(data)

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def test_onsetDate(self):
        assert_equal(self.parser.data['onsetDate'], datetime(2012, 10, 28, 3, 34, 51, tzinfo=tz.tzutc()))

    def test_expireDate(self):
        assert_equal(self.parser.data['expireDate'], datetime(2012, 10, 28, 5, 34, 51, tzinfo=tz.tzutc()))

    def test_update_flag(self):
        assert_true(self.parser.data['isUpdate'])

    def test_cancel_flag(self):
        assert_false(self.parser.data['isCancel'])

    def test_id(self):
        assert_equal(self.parser.data['id'], 'mcl1uw')

class Test_parse_real_cancel(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.parser = CapXMLReader()
        f = open(r'testdata/cancel.xml', 'r')
        data = f.read()
        f.close()
        self.parser.parse(data)

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.parser = None

    def test_onsetDate(self):
        assert_equal(self.parser.data['onsetDate'], datetime(2012, 10, 28, 11, 44, 34, tzinfo=tz.tzutc()))

    def test_expireDate(self):
        assert_equal(self.parser.data['expireDate'], datetime(2012, 10, 28, 14, 44, 34, tzinfo=tz.tzutc()))

    def test_update_flag(self):
        assert_true(self.parser.data['isUpdate'])

    def test_cancel_flag(self):
        assert_true(self.parser.data['isCancel'])

    def test_id(self):
        assert_equal(self.parser.data['id'], 'mcl1uw')

def test_parse_exercise_data():
    parser = CapXMLReader()
    f = open(r'testdata/exercise.xml', 'r')
    data = f.read()
    f.close()
    assert_false(parser.parse(data))
    assert_equal(parser.get_alert_data(), None)
    parser = None

def test_parse_invalid_data():
    parser = CapXMLReader()
    assert_false(parser.parse(r'<asdf>kjgkjsgd</asdf>'))
    assert_equal(parser.get_alert_data(), None)
