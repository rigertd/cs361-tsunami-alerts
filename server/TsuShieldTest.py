#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This performs unit tests for TsuShield.py
"""

import TsuShield
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import raises
from datetime import datetime
from dateutil.parser import parse

def do_download_happy_path():
    alert = do_download(False)
    assert_not_equal(alert, None)
    response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
	assert_equal(alert, response.read())

def do_download_test():
    alert = do_download(True)
    assert_not_equal(alert, None)
    with open(r'testdata/actual_not_expired.xml', 'r') as f:
        assert_equal(alert, f.read())

def test_alert_server_application_happy_path():
    url = 'http://vps54981.vps.ovh.ca:8080/?latitude=54.266701&longitude=-133.066696'
    
    response = urllib2.urlopen(url)
    alert = response.read()
    assert_not_equal(alert, None)
	
def test_alert_server_application_invalid_type():
    url = 'http://vps54981.vps.ovh.ca:8080/?latitude=foo&longitude=bar'
    
    response = urllib2.urlopen(url)
    alert = response.read()
    assert_not_equal(alert, None)
    assert_equal(alert,"Invalid coordinates. Cannot complete request.")
	
def test_alert_server_application_invalid_latitude():
    url = 'http://vps54981.vps.ovh.ca:8080/?latitude=91&longitude=1'
    
    response = urllib2.urlopen(url)
    alert = response.read()
    assert_not_equal(alert, None)
    assert_equal(alert,"Invalid coordinates. Cannot complete request.")
	
def test_alert_server_application_invalid_longitude():
    url = 'http://vps54981.vps.ovh.ca:8080/?latitude=1&longitude=-181'
    
    response = urllib2.urlopen(url)
    alert = response.read()
    assert_not_equal(alert, None)
    assert_equal(alert,"Invalid coordinates. Cannot complete request.")