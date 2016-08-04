#!/usr/bin/env python
"""
Class: CS361_400, SU2016
Group: Tsunami Alerts

This is the unit test code for the Alert
module.
"""
from Alert import Alert
from nose.tools import assert_equal
from nose.tools import assert_almost_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import raises
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset
from dateutil.tz import tzutc
#================================================
# Initialization Unit Tests
#================================================
def test_init_happy_path():
    alert = Alert({ 'id': None,
                    'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                    'expireDate': None,
                    'isUpdate': False,
                    'isCancel': False,
                    'locations':[] 
                  })
    assert_not_equal(alert, None)
    assert_equal(alert.onsetDate, parse("1997-07-16T19:20+01:00"))

@raises(TypeError)
def test_init_no_args():
    alert = Alert()
    assert_equal(alert, None)

def test_init_expireDate_happy_path():
    alert = Alert({ 'id': None,
                    'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                    'expireDate': datetime(1997, 7, 16, 21, 20, tzinfo=tzoffset(None, 3600)),
                    'isUpdate': False,
                    'isCancel': False,
                    'locations':[] 
                  })
    assert_not_equal(alert, None)
    assert_equal(alert.expireDate, parse("1997-07-16T21:20+01:00"))

@raises(TypeError)
def test_init_extra_arg():
    alert = Alert({}, "bar")
    assert_equal(alert, None)

#================================================
# Add and Remove Location Unit Tests
# Methods tested:
#   add_all_locations
#   add_location
#   remove_location
#================================================
class Test_add_and_remove_locations(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.alert = Alert({    'id': None,
                                'onsetDate': None,
                                'expireDate': None,
                                'isUpdate': False,
                                'isCancel': False,
                                'locations':[] 
                            })

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.alert = None

    def setUp(self):
        """
        Run before each test method is run
        """
        del self.alert.locations[:]

    def test_add_location_happy_path(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((00.00, 00.00))
        assert_equal(len(self.alert.locations), 1)

    def test_add_location_max_vals(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((90, 180))
        assert_equal(len(self.alert.locations), 1)    

    def test_add_location_min_vals(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((-90, -180))
        assert_equal(len(self.alert.locations), 1)    

    def test_add_location_latitude_too_high(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((91, 180))
        assert_equal(len(self.alert.locations), 0)      

    def test_add_location_latitude_too_low(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((-91, 180))
        assert_equal(len(self.alert.locations), 0)       

    def test_add_location_longitude_too_high(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((90, 181))
        assert_equal(len(self.alert.locations), 0)            

    def test_add_location_longitude_too_low(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((90, -181))
        assert_equal(len(self.alert.locations), 0)        

    def test_add_location_latitude_string(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location(('90', 180))
        assert_equal(len(self.alert.locations), 0)       

    def test_add_location_longitide_string(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location((90, '180'))
        assert_equal(len(self.alert.locations), 0)     

    def test_add_location_both_string(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location(('90', '180'))
        assert_equal(len(self.alert.locations), 0)     

    def test_add_location_both_non_numeric(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_location(('aaaa', 'bbbb'))
        assert_equal(len(self.alert.locations), 0)    

    def test_remove_location_happy_path(self):
        self.alert.add_location((00.00, 00.00))
        assert_equal(len(self.alert.locations), 1)
        self.alert.remove_location((00.00, 00.00))
        assert_equal(len(self.alert.locations), 0)

    def test_remove_location_not_present(self):
        self.alert.add_location((00.00, 00.00))
        assert_equal(len(self.alert.locations), 1)
        self.alert.remove_location((90.00, 90.00))
        assert_equal(len(self.alert.locations), 1)        

    def test_add_all_locations_happy_path(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_all_locations([(00.00, 00.00), (30.23, 40.89), (11.11,22.22)])
        assert_equal(len(self.alert.locations), 3)

    def test_add_all_locations_empty_list(self):
        assert_equal(len(self.alert.locations), 0)
        self.alert.add_all_locations([])
        assert_equal(len(self.alert.locations), 0)    

#================================================
# Update Unit Tests
# Methods tested:
#   update_onsetDate
#   update_expireDate
#   update_locations
#   update_alert
#================================================
class Test_updates(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.alert = Alert({    'id': 'testAlert',
                                'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                'expireDate': datetime(2000, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                'isUpdate': False,
                                'isCancel': False,
                                'locations':[] 
                            })

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.alert = None

    def setUp(self):
        """
        Run before each test method is run
        """
        del self.alert.locations[:]
        self.alert.add_all_locations([(00.00, 00.00), (11.11, 11.11)])
        self.alert.onsetDate = datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600))
        self.alert.expireDate = datetime(2000, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600))
        self.alert.isUpdate = False

    def test_update_onsetDate_happy_path(self):
        assert_equal(self.alert.onsetDate, parse("1997-07-16T19:20+01:00"))
        self.alert.update_onsetDate("1998-07-16T19:20+01:00")
        assert_equal(self.alert.onsetDate, parse("1998-07-16T19:20+01:00"))

    def test_update_expireDate_happy_path(self):
        assert_equal(self.alert.expireDate, parse("2000-07-16T19:20+01:00"))
        self.alert.update_expireDate("1997-08-16T19:20+01:00")
        assert_equal(self.alert.expireDate, parse("1997-08-16T19:20+01:00"))

    def test_update_locations_happy_path(self):
        assert_equal(len(self.alert.locations), 2)
        self.alert.update_locations([(90, 180)])
        assert_equal(len(self.alert.locations), 1)
        assert_true((90, 180) in self.alert.locations)
        assert_false((11.11, 11.11) in self.alert.locations)

    def test_update_alert_happy_path(self):
        self.alert.update_alert({   'id': 'testAlert',
                                    'onsetDate': datetime(1998, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                    'expireDate': datetime(1998, 7, 23, 19, 20, tzinfo=tzoffset(None, 3600)),
                                    'isUpdate': True,
                                    'locations': [(33.33, 33.33), (44.44, 44.44), (55.55, 55.55)]
                                })
        assert_equal(self.alert.onsetDate, parse("1998-07-16T19:20+01:00"))
        assert_equal(self.alert.expireDate, parse("1998-07-23T19:20+01:00"))
        assert_true(self.alert.isUpdate)
        assert_equal(len(self.alert.locations), 3)
        assert_false((11.11, 11.11) in self.alert.locations)
        assert_true((33.33, 33.33) in self.alert.locations)

    def test_update_alert_non_matching_id(self):
        self.alert.update_alert({   'id': 'differentAlert',
                                    'onsetDate': datetime(1998, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                    'expireDate': datetime(1998, 7, 23, 19, 20, tzinfo=tzoffset(None, 3600)),
                                    'isUpdate': True,
                                    'locations': [(33.33, 33.33), (44.44, 44.44), (55.55, 55.55)]
                                })
        assert_not_equal(self.alert.onsetDate, parse("1998-07-16T19:20+01:00"))
        assert_not_equal(self.alert.expireDate, parse("1998-07-23T19:20+01:00"))
        assert_false(self.alert.isUpdate)
        assert_not_equal(len(self.alert.locations), 3)
        assert_true((11.11, 11.11) in self.alert.locations)
        assert_false((33.33, 33.33) in self.alert.locations)

#================================================
# Get Unit Tests
# Methods tested:
#   get_id
#   get_onsetDate
#   get_expireDate
#   get_locations
#   get_isUpdate
#================================================
class Test_gets(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.alert = Alert({    'id': 'testAlert',
                                'onsetDate': datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                'expireDate': datetime(2000, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)),
                                'isUpdate': False,
                                'isCancel': False,
                                'locations':[] 
                            })
        self.alert.add_all_locations([(00.00, 00.00), (11.11, 11.11)])

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.alert = None

    def test_get_id_happy_path(self):
        assert_equal(self.alert.get_id(), 'testAlert')
        assert_equal(self.alert.get_id(), self.alert.id)

    def test_get_onsetDate_happy_path(self):
        assert_equal(self.alert.get_onsetDate(), datetime(1997, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)))
        assert_equal(self.alert.get_onsetDate(), self.alert.onsetDate)

    def test_get_expireDate_happy_path(self):
        assert_equal(self.alert.get_expireDate(), datetime(2000, 7, 16, 19, 20, tzinfo=tzoffset(None, 3600)))
        assert_equal(self.alert.get_expireDate(), self.alert.expireDate)

    def test_get_locations_happy_path(self):
        assert_equal(self.alert.get_locations(), [(00.00, 00.00), (11.11, 11.11)])
        assert_equal(self.alert.get_locations(), self.alert.locations)

    def test_get_isUpdate_happy_path(self):
        assert_equal(self.alert.get_isUpdate(), False)
        assert_equal(self.alert.get_isUpdate(), self.alert.isUpdate)

#================================================
# is_in_range and distance Unit Tests
#================================================   
class Test_is_in_range_and_distance(object):
    @classmethod
    def setup_class(self):
        """
        Setup code run before any tests are run
        """
        self.alert = Alert({    'id': None,
                                'onsetDate': None,
                                'expireDate': None,
                                'isUpdate': False,
                                'isCancel': False,
                                'locations':[] 
                            })

    @classmethod
    def teardown_class(self):
        """
        Teardown code run after all tests are run
        """
        self.alert = None

    def setUp(self):
        """
        Run before each test method is run
        """
        del self.alert.locations[:]
        self.alert.add_all_locations([(00.00, 00.00), (77.77, 77.77)])
        self.alert.isCancel = False

    def test_is_in_range_happy_path(self):
        assert_true(self.alert.is_in_range((00.00, 00.00), 1.0))
        assert_false(self.alert.is_in_range((90.00, 00.00), 1.0))

    def test_is_in_range_max(self):
        assert_true(self.alert.is_in_range((00.14, 00.00), 10.0))
        assert_false(self.alert.is_in_range((00.15, 00.00), 10.0))

    def test_is_in_range_negative_num(self):
        assert_false(self.alert.is_in_range((00.00, 00.00), -10.0))

    def test_is_in_range_canceled_alert(self):
        assert_true(self.alert.is_in_range(00.00, 00.00), 1.0)
        self.alert.isCancel = True
        assert_false(self.alert.is_in_range(00.00, 00.00), 1.0)

    def test_distance_happy_path(self):
        assert_almost_equal(self.alert.distance((00.00, 00.00)), 0)
        assert_almost_equal(self.alert.distance((00.14, 00.00)), 9.675790717)

