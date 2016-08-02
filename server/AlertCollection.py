#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This module contains class definitions for AlertCollection
class to track collections of alerts.
"""
from Alert import Alert
from datetime import datetime

class AlertCollection:
    """
    Holds collection of alerts

    Class variables:
    alerts -- list of Alert objects
    """
    def __init__(self):
        self.alerts = {}

    def add_alert_by_object(self, alert):
        """
        Adds passed-in alert object to AlertCollection.
        """
        self.alerts[alert.id] = alert

    def add_alert_by_config(self, config):
        """
        Creates an Alert from passed-in config and adds
        it to AlertCollection.
        """
        alert = Alert(config)
        self.add_alert_by_object(alert)

    def remove_alert_by_id(self, alertID):
        """
        Removes Alert from AlertCollection that matches
        the passed-in id.
        """
        del self.alerts[alertID]

    def get_alerts_in_range(self, location, mileRange):
        """
        Returns dictionary of Alerts keyed by alert id 
        that are within the passed-in mileRange of the
        passed-in location.
        """
        alertsInRange = []
        self.remove_expired_alerts()
        for alertID, alert in self.alerts.iteritems():
            if alert.is_in_range(location, mileRange):
                alertsInRange.append(alert)
        return alertsInRange

    def remove_expired_alerts(self):
        """
        Removes any Alerts from the AlertCollection that
        have an expireDate prior to the time the function
        is called.
        """
        nowDate = datetime.utcnow()
        alertsToRemove = []
        for alertID, alert in self.alerts.iteritems():
            if alert.get_expireDate() < nowDate:
                alertsToRemove.append(alertID)
        for i in alertsToRemove:
            self.remove_alert_by_id(i)


