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
from dateutil.tz import tzutc

class Alert:
    """
    Holds data for one alert

    Class variabls:
    id -- unique string identifier for the incident
    onsetDate -- datetime object for alert start date/time
    expireDate -- datetime object for alert end date/time
    locations -- list of tuples containing
                 latitude and longitude
    isUpdate -- boolean indicating if the alert is an
                update to an existing alert
    isCancel -- boolean indicating if the alert is a
                cancelation notice
    """
    def __init__(self, config):
        self.id = config['id']
        self.onsetDate = config['onsetDate']
        self.expireDate = config['expireDate']
        self.locations = []
        self.isUpdate = config['isUpdate']
        self.isCancel = config['isCancel']
        self.add_all_locations(config['locations'])

    def add_all_locations(self, locations):
        """
        Adds all location tuples from passed-in locations
        list to the Alert locations list
        """
        for location in locations:
            self.add_location(location)

    def add_location(self, location):
        """
        Adds passed-in location to the Alert location list
        """
        if location[0] <= 90 and location[0] >= -90 and location[1] <= 180 and location[1] >= -180:
            self.locations.append(location)

    def remove_location(self, location):    
        """
        Removes passed-in location tuple from the Alert
        location list
        """
        try:
            self.locations.remove(location)
        except ValueError:
            pass

    def update_onsetDate(self, onsetDate):
        """
        Updates Alert onsetDate to passed-in value
        """
        self.onsetDate = parse(onsetDate).astimezone(tzutc())

    def update_expireDate(self, expireDate):
        """
        Updates Alert expireDate to passed-in value
        """
        self.expireDate = parse(expireDate).astimezone(tzutc())

    def update_locations(self, locations):
        """
        Clears existing Alert location list and adds
        passed-in locations to list
        """
        del self.locations[:]
        self.add_all_locations(locations)

    def update_alert(self, config):
        """
        If Alert id matches passed-in value, updates 
        the Alert to passed-in values
        """
        if self.id == config['id']:
            self.onsetDate = config['onsetDate']
            self.expireDate = config['expireDate']
            self.update_locations(config['locations'])
            self.isUpdate = config['isUpdate']

    def get_id(self):
        return self.id

    def get_onsetDate(self):
        return self.onsetDate

    def get_expireDate(self):
        return self.expireDate

    def get_locations(self):
        return self.locations

    def get_isUpdate(self):
        return self.isUpdate

    def get_isCancel(self):
        return self.isCancel

    def is_in_range(self, pointLocation, mileRange):
        """
        Checks all Alert locations for range from
        passed-in location. If the alert is within 
        mileRange of passed-in location, returns true.
        """
        for location in self.locations:
            if not self.isCancel:
                if great_circle(location, pointLocation).miles <= mileRange:
                    print(great_circle(location, pointLocation).miles)
                    return True
        print(great_circle(location, pointLocation).miles)
        return False

    def distance(self, pointLocation):
        """
        Returns distance to closest location
        """
        distance = 100
        for location in self.locations:
            newDistance = great_circle(location, pointLocation).miles
            if newDistance < distance:
                distance = newDistance
        return distance
