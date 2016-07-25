#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module parses CapXML data and returns a WarningInfo object
for use in the Tsu-Shield server.
"""
from geopy.geocoders import Nominatim
from xml.etree import ElementTree

class WarningInfo:
    """
    Represents a tsunami warning announcement with the following attributes:
        - date: Date the warning was issued
        - areas: List of affected locations by latitude and longitude
    """
    def __init__(self, date):
        self.date = date
        self.areas = []
        self.locator = Nominatim()

    def add_area(self, lat, long):
        """
        Adds a location to the list of affected areas based on the latitude and longitude.
        Does not add the location if the specified latitude and longitude are invalid.
        """
        if lat <= 90 and lat >= -90 and long <= 180 and long >= -180:
            self.areas.append({'latitude':lat, 'longitude':long})

    def add_area(self, address):
        """
        Adds a location to the list of affected areas based on an address.
        Does not add the location if the address is invalid.
        """
        location = self.locator.geocode(address)
        if location:
            self.areas.append({'latitude':location.latitude, 'longitude':location.longitude})

def parseCapXML(raw_CapXML):
    """
    Parses CapXML data and returns a WarningInfo object.
    """
    alert = ElementTree.fromstring(raw_CapXML)
    date = alert.find("sent")
    if not date:
        return None
    info = WarningInfo(date.text)

    return info
