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
from multiprocessing import Process, Lock


mutex = Lock()

def main():
    alerts = AlertCollection()
    reader = CapXMLReader()
    
    polling_process = Process(target=download_alert_data, args=(reader, alerts,))
    polling_process.start()
    
    while True:
        pass
        time.sleep(300)

def download_alert_data(reader, container):
    while True:
        #response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
        #alert = response.read()
        with open(r'testdata/actual.xml', 'r') as f:
            alert = f.read()

        if reader.parse(alert):
            print "getting alert data"
            alertConfig = reader.get_alert_data()
            with mutex:
                print "adding data to container"
                container.add_alert_by_config(alertConfig)

        time.sleep(300)

if __name__ == '__main__':
    main()