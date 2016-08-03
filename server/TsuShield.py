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
from threading import Thread
import webapp2
from paste import httpserver
import json

alerts = AlertCollection()

class AlertServerApplication(webapp2.RequestHandler):
    def get(self):
        global alerts
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            self.response.write("Invalid coordinates. Cannot complete request.")
            return
            
        if latitude > 90 or latitude < -90:
            self.response.write("Invalid coordinates. Cannot complete request.")
            return
        elif longitude > 180 or longitude < -180:
            self.response.write("Invalid coordinates. Cannot complete request.")
            return

        alertsInRange = alerts.get_alerts_in_range((latitude, longitude), 10.0)
        if len(alertsInRange) == 0:
            jsonResponse = { 'activeAlert': False, 'distance': None }
            self.response.write(json.dumps(jsonResponse))
            return

        minDist = 100
        for alert in alertsInRange:
            newDist = alert.distance((latitude, longitude))
            if newDist < minDist:
                minDist = newDist

        jsonResponse = { 'activeAlert': True, 'distance': minDist }
        self.response.write(json.dumps(jsonResponse))

app = webapp2.WSGIApplication([('/', AlertServerApplication),], debug=True)


def main():
    reader = CapXMLReader()
    thread = Thread(target=download_alert_data, args=(reader,))
    thread.daemon = True
    thread.start()

    httpserver.serve(app, host='158.69.197.74', port='8080', daemon_threads=True)    
    

def download_alert_data(reader):
    global alerts
    while True:
        #response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
        #alert = response.read()
        with open(r'testdata/actual_not_expired.xml', 'r') as f:
            alert = f.read()

        if reader.parse(alert):
            print "getting alert data"
            alertConfig = reader.get_alert_data()
            #with mutex:
            print "adding data to container"
            alerts.add_alert_by_config(alertConfig)

        time.sleep(300)

if __name__ == '__main__':
    main()
