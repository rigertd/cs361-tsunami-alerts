#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the AlertCollection
module.
"""
import AlertCollection
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
	alertCollection = AlertCollection()
	assert_not_equal(alertCollection, None)
	assert_equal(len(alertCollection.alerts), 0)

@raises(TypeError)
def test_init_extra_arg():
	alertCollection = AlertCollection("bar")
	assert_equal(alertCollection, None)

def test_add_alert_happy_path():
	alertCollection = AlertCollection()
	assert_equal(len(alertCollection.alerts), 0)
	alert = Alert("1997-07-16T19:20+01:00")
	alertCollection.add_alert(alert)
	assert_equal(len(alertCollection.alerts), 1)

def test_remove_alert_happy_path():
	alertCollection = AlertCollection()
	alert = Alert("1997-07-16T19:20+01:00")
	alertCollection.add_alert(alert)
	assert_equal(len(alertCollection.alerts), 1)
	alertCollection.remove_alert(alert)
	assert_equal(len(alertCollection.alerts), 0)