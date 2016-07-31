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
	"""
	def __init__(self, config):
        self.id = config['id']
		self.onsetDate = config['onsetDate']
		self.expireDate = config['expireDate']
		self.locations = []
		self.isUpdate = config['isUpdate']
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
		self.locations.append(location)

	def remove_location(self, location):	
		"""
		Removes passed-in location tuple from the Alert
		location list
		"""
		self.locations.remove(location)

	def update_onsetDate(self, onsetDate):
		"""
		Updates Alert onsetDate to passed-in value
		"""
		self.onsetDate = onsetDate

	def update_expireDate(self, expireDate):
		"""
		Updates Alert expireDate to passed-in value
		"""
		self.expireDate = expireDate

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
			self.update_onsetDate(config['onsetDate'])
			self.update_expireDate(config['expireDate'])
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

	def is_in_range(self, pointLocation, mileRange):
		"""
		Checks all Alert locations for range from
		passed-in location. If the alert is within 
		mileRange of passed-in location, returns true.
		"""
		for location in self.locations:
			if great_circle(location, pointLocation).miles <= mileRange:
				return true
		return false


