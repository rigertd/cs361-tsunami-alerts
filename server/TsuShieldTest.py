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

def test_download_alert_data():
    assert_not_equal(alert, None)

app = webapp2.WSGIApplication([('/', AlertServerApplication),], debug=True)
host = '158.69.197.74'
port = '8080'
httpserver.serve(app, host, port)

def test_download_alert_data_happy_path():
    assert_not_equal(alerts, None)
	
	
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