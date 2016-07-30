#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module contains class definitions for Alert
class to track individual alerts.
"""
from datetime import datetime
from dateutil.parser import parse
from geopy.distance import great_circle
from AlertCollection import AlertCollection
import urllib2
from CapXMLReader import CapXMLReader
from Alert import Alert
from AlertCollection import AlertCollection

def main():
    alerts = AlertCollection()
    reader = CapXMLReader()
    
    #print great_circle((0.0,0.0),(0.14,0.0)).miles
    response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
    alert = response.read()
    reader.parse(alert)



if __name__ == '__main__':
    main()