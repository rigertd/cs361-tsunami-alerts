#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module contains class definitions for AlertCollection
class to track collections of alerts.
"""
import Alert

class AlertCollection:
	"""
	Holds collection of alerts

	Class variables:
	alerts -- list of Alert objects
	"""
	def __init__(self):
		self.alerts = {}

	def add_alert(self, alert):
		self.alerts[alert.id] = alert

	def remove_alert(self, alert):
        del self.alerts[alert.id]