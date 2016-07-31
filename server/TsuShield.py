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
import time

def main():
    alerts = AlertCollection()
    reader = CapXMLReader()
    
    while True:
        response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
        alert = response.read()

        if reader.parse(alert):
            alertConfig = reader.get_alert_data()
            alerts.add_alert_by_config(alertConfig)

        

        time.sleep(300)

if __name__ == '__main__':
    main()