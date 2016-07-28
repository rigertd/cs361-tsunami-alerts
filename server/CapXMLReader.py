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
        if lat <= 90 and lat >= -90 and long <= 180 and long >= -180:
            self.data['areas'].append({'latitude':lat, 'longitude':long})
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
            self.data['areas'].append({'latitude':location.latitude, 'longitude':location.longitude})
            return True
        else:
            return False

    def initialize(self):
        """
        Initializes all of the member variables of the object.
        """
        self.data = { 'date': None, 'areas':[] }

    def parse(self, raw_CapXML):
        """
        Parses CapXML data and stores it as a python dictionary object
        with the following structure:
        
        { date: (issue alert date and time),
          areas: [ { latitude:#.##, longitude:#.## }, ... ] }
        """
        
        return False

    def get_alert_data(self):
        """
        Gets the parsed CapXML data held by the object
        """

    def reset(self):
        """
        Resets the reader object to its initial empty state.
        """
        self.initialize()
