#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module contains class definitions for Alert
class to track individual alerts.
"""
from datetime import datetime
from dateutil.parser import parse

class Alert:
	"""
	Holds data for one alert

	Class variabls:
	onsetDate -- datetime object for alert start date/time
	expireDate -- datetime object for alert end date/time
	locations -- list of dictionary objects containing
				 latitude and longitude
	"""
	def __init__(self, onsetDate, expireDate=None):
		self.onsetDate = parse(onsetDate)
		self.expireDate = parse(expireDate)
		self.locations = []

	def add_location(self, latitude, longitude):
		location = { "latitude": latitude, "longitude": longitude }
		self.locations.append(location)

	def remove_location(self, latitude, longitude):

	def update_onsetDate(self, onsetDate):

	def update_expireDate(self, expireDate):
