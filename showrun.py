#python 3.5.2
import pexpect
import sys
import os

device_list = list()
device_info = {}
file = open('devices.txt','r')
for device in file:
    device_info=device.split(',')
    ip = device_info[0]
    username = device_info[1]
    password = device_info[2]
    enable   = device_info[3]
    hostname = device_info[4]
    hostname = hostname.strip()
##  connect session and send commands
    session = pexpect.spawn('telnet ' + ip, timeout=20)
    session.maxread=9999999
    #session.logfile = sys.stdout
    result = session.expect(['Username:', pexpect.TIMEOUT])
    if result != 0:
        print ("fail on ", ip)
        exit()
    session.sendline(username)
    result = session.expect(['Password:'])
    if result != 0:
        print ("fail on ", ip)
        exit()
    session.sendline(password)
    result = session.expect(['>', pexpect.TIMEOUT])
    if result != 0:
        print ("fail on ", ip)
        exit()
    session.sendline('enable')
    result = session.expect(['Password:', pexpect.TIMEOUT])
    if result != 0:
         print ("fail on ", ip)
         exit()
    session.sendline(enable)
    result = session.expect(['#', pexpect.TIMEOUT])
    if result != 0:
        print ("fail on ", ip)
        exit()
    session.sendline('sh run | i hostname')
    result = session.expect([hostname+'#', pexpect.TIMEOUT])
    if result != 0:
        print ("fail on ", ip)
        print (hostname+'#')
        exit()
    output = session.before
    print(output.decode('utf-8'))
    session.close
file.close()
