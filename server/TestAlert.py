#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the Alert
module.
"""
from Alert import Alert
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import raises
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset
from dateutil.tz import tzutc
#================================================
# Initialization Unit Tests
#================================================
def test_init_happy_path():
    alert = Alert({ 'id': None,
                    'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                    'expireDate': None,
                    'isUpdate': False,
                    'isCancel': False,
                    'locations':[] 
                  })
    assert_not_equal(alert, None)
    assert_equal(alert.onsetDate, parse("1997-07-16T19:20+01:00"))

@raises(TypeError)
def test_init_no_args():
    alert = Alert()
    assert_equal(alert, None)

def test_init_expireDate_happy_path():
    alert = Alert({ 'id': None,
                    'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                    'expireDate': datetime(1997, 7, 16, 21, 20, tzinfo=tzoffset(None, 3600)),
                    'isUpdate': False,
                    'isCancel': False,
                    'locations':[] 
                  })
    assert_not_equal(alert, None)
    assert_equal(alert.expireDate, parse("1997-07-16T21:20+01:00"))

@raises(TypeError)
def test_init_extra_arg():
    alert = Alert({}, "bar")
    assert_equal(alert, None)

#================================================
# Add and Remove Location Unit Tests
# Methods tested:
#   add_all_locations
#   add_location
#   remove_location
#================================================
class Test_add_and_remove_locations(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """

    def setUp(self):
        """
        Run before each test method is run
        """

    def test_add_location_happy_path():
        alert = Alert({ 'id': None,
                        'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)).astimezone(tzutc()),
                        'expireDate': None,
                        'isUpdate': False,
                        'isCancel': False,
                        'locations':[] 
                      })
        assert_equal(len(alert.locations), 0)
        alert.add_location((00.00, 00.00))
        assert_equal(len(alert.locations), 1)

    def test_remove_location_happy_path():
        alert = Alert({ 'id': None,
                        'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)).astimezone(tzutc()),
                        'expireDate': None,
                        'isUpdate': False,
                        'isCancel': False,
                        'locations':[] 
                      })
        alert.add_location((00.00, 00.00))
        assert_equal(len(alert.locations), 1)
        alert.remove_location((00.00, 00.00))
        assert_equal(len(alert.locations), 0)

#================================================
# Update Unit Tests
# Methods tested:
#   update_onsetDate
#   update_expireDate
#   update_locations
#   update_alert
#================================================
class Test_updates(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """

    def setUp(self):
        """
        Run before each test method is run
        """

    def test_update_onsetDate_happy_path():
        alert = Alert({ 'id': None,
                        'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                        'expireDate': None,
                        'isUpdate': False,
                        'isCancel': False,
                        'locations':[] 
                      })
        assert_equal(alert.onsetDate, parse("1997-07-16T19:20+01:00"))
        alert.update_onsetDate("1998-07-16T19:20+01:00")
        assert_equal(alert.onsetDate, parse("1998-07-16T19:20+01:00"))

    def test_update_expireDate_happy_path():
        alert = Alert({ 'id': None,
                        'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                        'expireDate': datetime(2000, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                        'isUpdate': False,
                        'isCancel': False,
                        'locations':[] 
                      })
        assert_equal(alert.expireDate, parse("2000-07-16T19:20+01:00"))
        alert.update_expireDate("1997-08-16T19:20+01:00")
        assert_equal(alert.expireDate, parse("1997-08-16T19:20+01:00"))

#================================================
# Get Unit Tests
# Methods tested:
#   get_id
#   get_onsetDate
#   get_expireDate
#   get_locations
#   get_isUpdate
#================================================
class Test_gets(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """

    def setUp(self):
        """
        Run before each test method is run
        """

#================================================
# is_in_range Unit Tests
#================================================   
class Test_is_in_range(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """

    def setUp(self):
        """
        Run before each test method is run
        """