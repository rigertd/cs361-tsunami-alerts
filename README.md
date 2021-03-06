```
Group:       Tsunami Alerts (14)
Date:        8/6/2016
Class:       CS361 Summer 2016
Description: Setup Instructions for Project B
```

=================================================
Tsu-Shield Server
=================================================
This program provides a REST API that can be used to determine
whether there is an active tsunami alert within 10 miles of
a specified geolocation.

**INSTALLATION REQUIREMENTS**

1. Super user/administrator permissions
2. Python 2.7

**ENVIRONMENT SETUP**

1. Navigate to the `server` directory.
2. Type `sudo pip install -r requirements.txt` to install all dependencies.

**SERVER USAGE INSTRUCTIONS**

1. Start the server with the following syntax:
>  ./TsuShield.py [server_ip_addr] [server_port_num] [-t]

2. To shut down the server, press Ctrl+C.
   This disconnects any connected clients and aborts all transfers.

*  Specify the public IP address of the server and the port number
   to listen on. If you do not specify these values, the server will
   only be accessible at http://127.0.0.1:8080.
*  The `-t` argument tells the server to read test data instead of the
   actual alert feed from the NOAA website. The test data has a tsunami
   alert in effect for the following coordinates:
   - Latitude:  54.266701
   - Longitude: -133.066696
*  An instance of the server is already running in test mode at
   http://vps54981.vps.ovh.ca:8080.
   You can use this instance if you do not have the permissions required
   to setup the Python environment and run a web server.

**SERVER UNIT TESTS**

1. Navigate to the `server` directory.
2. Type `nosetests -v` to start the unit tests.

**FRONT END USAGE INSTRUCTIONS**

1. Plop it into your favorite directory
2. Open index.html
3. Click (on Chrome) F12, Ctrl+Shift+M to get the proper responsive web page, as it would appear on a mobile device.
4. Special Note: inputting 54.266701 as the latitude and -133.066696 as the longitude will show an example of a true alert response
5. inputs must be real numbers.
6. A hosted version can be reached at: http://web.engr.oregonstate.edu/~bergmkyl/cs361-tsunami-alerts/front-end/

