# -*- coding: utf-8 -*-
#!/usr/bin/env python

import httplib, urllib
import time


def connect(ip):    
    headers = {"Content-type":"application/x-www-form-urlencoded"}   
    
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
        
        'provider':'OSU username'
    }
    
    params['userip'] = ip
    params["username"] = username
    params["password"] = password

    # Connection request
    h = httplib.HTTPSConnection("be4cas03.resnet.ohio-state.edu")     
    
    h.request("POST", "/auth/perfigo_cm_validate.jsp", urllib.urlencode(params), headers)

    h.getresponse().read()


# Start of program
username = raw_input("What is your OSU Name.#? ")
password = raw_input("What is your OSU password (Beware of those standing behind you)? ")

print ""

ip = raw_input("Enter other device's IP Address: ")

print ""

cont = raw_input("Run continuously [Y/n]? ")

print ""

if cont[0].capitalize() == "Y":
    while True:
        print time.strftime("%H:%M")
        connect(ip)
        
        time.sleep(60.0)
else:
    connect(ip)
    print "Sent connection request"
