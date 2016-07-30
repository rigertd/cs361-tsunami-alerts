#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module implements a facade for reading CapXML data, 
extracting the required information, and converting it to
a standardized format for use in the Tsu-Shield system.
"""
from geopy.geocoders import Nominatim
from xml.etree import ElementTree
from datetime import datetime
from dateutil import tz
from dateutil import parser
import re

class CapXMLReader:
    """
    Parses and converts CapXML data.
    """
    def __init__(self):
        self.locator = Nominatim()
        self.initialize()

    def add_by_lat_long(self, lat, long):
        """
        Adds a location to the list of affected areas based on the latitude and longitude.
        Does not add the location if the specified latitude and longitude are invalid.
        """
        try:
            latitude = float(lat)
            longitude = float(long)
        except ValueError:
            return False

        if latitude <= 90 and latitude >= -90 and longitude <= 180 and longitude >= -180:
            self.data['locations'].append((latitude, longitude))
            return True
        else:
            return False

    def add_by_address(self, address):
        """
        Adds a location to the list of affected areas based on an address.
        Does not add the location if the address is invalid.
        """
        location = self.locator.geocode(address)
        if location:
            self.data['areas'].append((location.latitude, location.longitude))
            return True
        else:
            return False

    def initialize(self):
        """
        Initializes all of the member variables of the object.
        """
        self.data = { 'id': None,
                      'onsetDate': None,
                      'expireDate': None,
                      'isUpdate': False,
                      'locations':[] 
                    }

    def parse(self, raw_CapXML):
        """
        Parses CapXML data and stores it as a python dictionary object
        with the following structure:
        
        { id: (incident id string),
          onsetDate: (issue alert date and time),
          expireDate: (date and time alert expires),
          isUpdate: (msgType == Update)
          locations: [ ( latitude #.##, longitude #.## ), ... ] }
        """
        raw_CapXML = re.sub(r'\s+xmlns="[^"]+"', '', raw_CapXML)
        root = ElementTree.fromstring(raw_CapXML)
        
        if root is None:
            print "Invalid XML"
            return False
        
        if root.tag != 'alert':
            print root.tag
            print "Not an alert"
            return False
        
        status = root.find('status')
        if status is None or status.text != 'Actual':
            print "Not actual alert"
            return False
        
        incident = root.find('incidents')
        if incident is None:
            print "Incident ID not found"
            return False
        self.data['id'] = incident.text.strip()
            
        msgType = root.find('msgType')
        if msgType is None:
            print "Message type not found"
            reset()
            return False
        self.data['isUpdate'] = msgType.text == 'Update'
        
        info = root.find('info')
        if info is None:
            print "Message info not found"
            reset()
            return False
        
        event = info.find('event')
        if event is None or event.text != 'Tsunami':
            print "Event type not found or not Tsunami"
            reset()
            return False
        
        onsetDate = info.find('onset')
        if onsetDate is None:
            print "Onset date not found"
            reset()
            return False
        try:
            date = parser.parse(onsetDate.text)
            self.data['onsetDate'] = date
        except ValueError:
            print "Invalid onset date"
            reset()
            return False
        
        expireDate = info.find('expires')
        if expireDate is None:
            print "Expire date not found"
            reset()
            return False
        try:
            date = parser.parse(expireDate.text)
            self.data['expireDate'] = date
        except ValueError:
            print "Invalid expire date"
            reset()
            return False
            
        for area in info.iterfind('area'):
            circle = area.find('circle')
            if circle is None:
                print "Coordinates not found for ", area.find('areaDesc').text
                pass
            lat, long = self.convert_circle(circle.text)
            self.add_by_lat_long(lat, long)

    def convert_circle(self, text):
        return tuple(text.split(' ')[0].split(','))
            
    def get_alert_data(self):
        """
        Gets the parsed CapXML data held by the object
        """
        return self.data

    def reset(self):
        """
        Resets the reader object to its initial empty state.
        """
        self.initialize()
