# -*- coding: utf-8 -*-
#!/usr/bin/env python

import http.client as http
import urllib, socket, time, sys, getopt


def connect(ip, username, password):    
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
    
    params = urllib.parse.urlencode(params)

    print("IP is: " + ip)

    # Connection request
    h = http.HTTPSConnection("be4cas03.resnet.ohio-state.edu", timeout=5)     
    
    h.request("POST", "/auth/perfigo_cm_validate.jsp", params, headers)

    h.getresponse().read()


def test_connection():
    connected = False    
    
    # Google test
    h2 = httplib.HTTPConnection("www.google.com")

    h2.request("GET", "/")

    data = h2.getresponse().read()
    
    # Test to see if a real reply from Google was recieved
    if not "ohio-state" in data:
        print("Connected!")
        connected = True
    else:
        print("No connection")
        
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

def main(argv=None):
    try:
        opts, args = getopt.getopt(argv,"u:p:c",["username=","password="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    cont = False
    username = ""
    password = ""

    given = [False, False, False]    
    
    for o, a in opts:
        if o in ("-u", "--username"):
            username = a
            given[0] = True
        elif o in ("-p", "--password"):
            password = a
            given[1] = True
        elif o == "-c":
            cont = True
            given[2] = True
    
    if not given[0]:
        username = input("What is your OSU Name.#? ")
        
    if not given[1]:
        password = input("What is your OSU password (Beware of those standing behind you)? ")
    
    ip = get_local_ip() 
    
    if cont:
        while True:
            print(time.strftime("%H:%M"))
            if not test_connection():
                connect(ip, username, password)
            
            time.sleep(60.0)
    else:
        connect(ip, username, password)
        test_connection()
    
if __name__ == "__main__":
    main(sys.argv[1:])
