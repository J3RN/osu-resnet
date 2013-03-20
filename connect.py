# -*- coding: utf-8 -*-
#!/usr/bin/env python

import httplib, urllib
import socket
import time


def connect():    
    headers = {"Content-type":"application/x-www-form-urlencoded"}
    
    ip = get_local_ip()    
    
    params = {
        'reqFrom':'perfigo_login.jsp',
        'uri':'',
        'cm':'',
        'session':'',
        'pm':'',
        'index':'1',
        'pageid':'-1',
        'compact':'false',
        
        'registerGuest':'NO',
        'userNameLabel':'OSU name.# (lowercase)',
        'passwordLabel':'Password',
        'guestUserNameLabel':'Guest ID',
        'guestPasswordLabel':'Password',
        
        'username':'\'' + username + '\'',
        'password':'\'' + password + '\'',
        
        'provider':'OSU username'
    }
    
    params['userip'] = ip
    params["username"] = username
    params["password"] = password
    
    print "IP is: " + ip

    # Connection request
    h = httplib.HTTPSConnection("be4cas03.resnet.ohio-state.edu")     
    
    h.request("POST", "/auth/perfigo_cm_validate.jsp", urllib.urlencode(params), headers)

    h.getresponse().read()


def test_connection():
    connected = False    
    
    # Google test
    h2 = httplib.HTTPConnection("www.google.com")

    h2.request("GET", "/")

    data = h2.getresponse().read()
    
    # Test to see if a real reply from Google was recieved
    if not "ohio-state" in data:
        print "Connected!"
        connected = True
    else:
        print "No connection"
        
    return connected


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    host = "www.google.com"
    
    try:
        s.connect((host, 9))
        client = s.getsockname()[0]
    except socket.error:
        client = "Unknown IP"
    finally:
        del s
        
    return client


# Start of program
username = raw_input("What is your OSU Name.#? ")
password = raw_input("What is your OSU password? (Beware of those standing behind you) ")

print ""

cont = raw_input("Run continuously? (Y/n) ")

print ""

if cont.capitalize() == "Y":
    while True:
        print time.strftime("%H:%M")
        if not test_connection():
            connect()
        
        time.sleep(60.0)
else:
    connect()
    test_connection()
