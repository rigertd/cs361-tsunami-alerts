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
import webapp2
from paste import httpserver
import json

mutex = Lock()
alerts = AlertCollection()


class AlertServerApplication(webapp2.RequestHandler):
    def get(self):
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')
        print(latitude + " " + longitude)

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            self.response.write("Invalid coordinates. Cannot complete request.")
            return

        alertsInRange = alerts.get_alerts_in_range((latitude, longitude), 10.0)
        if len(alertsInRange) == 0:
            jsonResponse = { 'activeAlert': False, 'distance': None }
            self.response.write(json.dumps(jsonResponse))
            print(str(latitude) + " " + str(longitude))
            return

        minDist = 100
        for alert in alertsInRange:
            newDist = alert.distance()
            if newDist < minDist:
                minDist = newDist

        jsonResponse = { 'activeAlert': True, 'distance': minDist }
        self.response.write(json.dumps(jsonResponse))

app = webapp2.WSGIApplication([('/', AlertServerApplication),], debug=True)

def main():
    reader = CapXMLReader()
    polling_process = Process(target=download_alert_data, args=(reader, alerts,))
    polling_process.start()

    httpserver.serve(app, host='158.69.197.74', port='8080')    
    

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
