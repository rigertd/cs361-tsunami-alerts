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
from threading import Thread, Lock
import webapp2
from paste import httpserver
import json
from argparse import ArgumentParser

alerts = AlertCollection()
mutex = Lock()

class AlertServerApplication(webapp2.RequestHandler):
    def get(self):
        global alerts
        global mutex
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')

        self.response.headers.add_header('Access-Control-Allow-Origin', '*')

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

        with mutex:
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
    args = parse_args()
    thread = Thread(target=download_alert_data, args=(args.test,),)
    thread.daemon = True
    thread.start()

    time.sleep(1)
    print "Press Ctrl-C to shutdown"
    httpserver.serve(app, host=args.ip_addr, port=args.port, daemon_threads=True)


def check_for_alert_data(isTest):
    global alerts
    global mutex
    reader = CapXMLReader()
    alert = download_alert_data(isTest)

def do_download(isTest):
    if not isTest:
        print "Downloading alert data from NOAA"
        response = urllib2.urlopen('http://wcatwc.arh.noaa.gov/events/xml/PAAQCAP.xml')
        return response.read()
    else:
        print "Opening test alert data"
        with open(r'testdata/actual_not_expired.xml', 'r') as f:
            return f.read()

def download_alert_data(isTest):
    global alerts
    global mutex
    reader = CapXMLReader()
    while True:
        alert = do_download(isTest)

        if reader.parse(alert):
            alertConfig = reader.get_alert_data()
            with mutex:
                print "adding data to container"
                alerts.add_alert_by_config(alertConfig)

        time.sleep(300)

def parse_args():
    """
    Configures an ArgumentParser and uses it to parse the command line options.

    Returns an object containing the argument data.
    """
    parser = ArgumentParser(description='TsuShield server application.')
    parser.add_argument('ip_addr', help='The IP address of the server hosting the TsuShield API.', nargs='?', default='127.0.0.1')
    parser.add_argument('port', help='The port number on which to host the TsuShield API.', nargs='?', default='8080')
    parser.add_argument('-t', '--test', help='Use test data to simulate active tsunami alert', action='store_true')
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()
