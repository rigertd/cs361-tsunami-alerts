#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the CapXML parser module.
"""
import tsu_parser as parser
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import datetime

class TestWarningInfo(object):
    @classmethod
    def setup_class(obj):
        """
        Setup code run before any tests are run
        """
        
    @classmethod
    def teardown_class(obj):
        """
        Teardown code run after all tests are run
        """
        
    def setUp(self):
        """
        Run before each test method is run
        """

    def tearDown(self):
        """
        Run after each test method is run
        """
        
    def test_init_happy_path(self):
        date = '2012-10-28T03:07:27-00:00'
        info = parser.WarningInfo(date)
        assert_equal(date, info.date)
        assert_not_equal('2012-10-28T03:07:00-00:00', info.date)
    
    @raises(TypeError)
    def test_init_no_date(self):
        info = parser.WarningInfo()

    def test_add_area_long_lat_happy_path(self):
        info = parser.WarningInfo('2012-10-28T03:07:27-00:00')
        info.add_area('44.564089096,-123.28061099')
        assert_equal(len(info.areas), 1) # one item
        assert_almost_equal(info.areas[0]['latitude'], 44.564089096)
        assert_almost_equal(info.areas[0]['longitude'], -123.28061099)
        
    def test_add_area_address_happy_path(self):
        info = parser.WarningInfo('2012-10-28T03:07:27-00:00')
        info.add_area('Corvallis, OR 97331')
        assert_equal(len(info.areas), 1) # one item
        assert_almost_equal(info.areas[0]['latitude'], 44.564089096)
        assert_almost_equal(info.areas[0]['longitude'], -123.28061099)
    
    def test_add_area_address_invalid_address(self):
        info = parser.WarningInfo('2012-10-28T03:07:27-00:00')
        info.add_area('adskfjs;ldkjf;lkasjdf')
        assert_equal(len(info.areas), 0) # Should be empty
    