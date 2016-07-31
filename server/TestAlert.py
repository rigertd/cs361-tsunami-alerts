#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the Alert
module.
"""
import Alert
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import raises
from datetime import datetime
from dateutil.parser import parse
#================================================
# Initialization Unit Tests
#================================================
def test_init_happy_path():
    alert = Alert("1997-07-16T19:20+01:00")
    assert_not_equal(alert, None)
    assert_equal(alert.onsetDate, parse("1997-07-16T19:20+01:00"))

@raises(TypeError)
def test_init_no_args():
    alert = Alert()
    assert_equal(alert, None)

def test_init_expireDate_happy_path():
    alert = Alert("1997-07-16T19:20+01:00", "1997-07-16T21:20+01:00")
    assert_not_equal(alert, None)
    assert_equal(alert.expireDate, parse("1997-07-16T21:20+01:00"))

@raises(TypeError)
def test_init_extra_arg():
    alert = Alert("1997-07-16T19:20+01:00", "1997-07-16T21:20+01:00", "bar")
    assert_equal(alert, None)

def test_add_location_happy_path():
    alert = Alert("1997-07-16T19:20+01:00")
    assert_equal(len(alert.locations), 0)
    alert.add_location(00.00, 00.00)
    assert_equal(len(alert.locations), 1)

def test_remove_location_happy_path():
    alert = Alert("1997-07-16T19:20+01:00")
    alert.add_location(00.00, 00.00)
    assert_equal(len(alert.locations), 1)
    alert.remove_location(00.00, 00.00)
    assert_equal(len(alert.locations), 0)

def test_update_onsetDate_happy_path():
    alert = Alert("1997-07-16T19:20+01:00")
    assert_equal(alert.onsetDate, parse("1997-07-16T19:20+01:00"))
    alert.update_onsetDate("1998-07-16T19:20+01:00")
    assert_equal(alert.onsetDate, parse("1998-07-16T19:20+01:00"))

def test_update_expireDate_happy_path():
    alert = Alert("1997-07-16T19:20+01:00", "2000-07-16T19:20+01:00")
    assert_equal(alert.expireDate, parse("2000-07-16T19:20+01:00"))
    alert.update_expireDate("1997-08-16T19:20+01:00")
    assert_equal(alert.expireDate, parse("1997-08-16T19:20+01:00"))