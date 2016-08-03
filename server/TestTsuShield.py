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
import webapp2
from paste import httpserver
import urllib2
from threading import Thread

def start_local_http_server():
    app = webapp2.WSGIApplication([('/', TsuShield.AlertServerApplication),], debug=True)
    host = '127.0.0.1'
    port = '8080'
    httpserver.serve(app, host, port, daemon_threads=True)

class TestTsuShield(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        thread = Thread(target=start_local_http_server,)
        thread.daemon = True
        thread.start()
        loop = True
        count = 10
        while loop:
            try:
                urllib2.urlopen('http://127.0.0.1:8080')
                print "Opened URL--server is running"
                loop = False
            except urllib2.URLError:
                print "Cannot connect yet"
                if count > 0:
                    count -= 1
                else:
                    print "Web server failed to start"
                    loop = False

    def test_alert_server_application_happy_path(self):
        url = 'http://127.0.0.1:8080/?latitude=54.266701&longitude=-133.066696'
        
        response = urllib2.urlopen(url)
        assert_equal(response.getcode(), 200)
        alert = response.read()
        assert_not_equal(alert, None)
        
    def test_alert_server_application_invalid_type(self):
        url = 'http://127.0.0.1:8080/?latitude=foo&longitude=bar'
        
        response = urllib2.urlopen(url)
        alert = response.read()
        assert_equal(response.getcode(), 200)
        assert_not_equal(alert, None)
        assert_equal(alert,"Invalid coordinates. Cannot complete request.")
        
    def test_alert_server_application_invalid_latitude(self):
        url = 'http://127.0.0.1:8080/?latitude=91&longitude=1'
        
        response = urllib2.urlopen(url)
        alert = response.read()
        assert_equal(response.getcode(), 200)
        assert_not_equal(alert, None)
        assert_equal(alert,"Invalid coordinates. Cannot complete request.")
        
    def test_alert_server_application_invalid_longitude(self):
        url = 'http://127.0.0.1:8080/?latitude=1&longitude=-181'
        
        response = urllib2.urlopen(url)
        alert = response.read()
        assert_equal(response.getcode(), 200)
        assert_not_equal(alert, None)
        assert_equal(alert,"Invalid coordinates. Cannot complete request.")