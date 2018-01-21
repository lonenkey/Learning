#python 3.5.2
import pexpect

device_list = list()
device_info = {}
file = open('devices.txt','r')
for device in file:
    device_info=device.split(',')
    ip = device_info[0]
    username = device_info[1]
    password = device_info[2]
    enable   = device_info[3]
##  connect session and send commands
    session = pexpect.spawn('telnet ' + ip, timeout=20)
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
    print ("You're clear kid.  Now blow this thing and lets go home.")
    session.sendline('enable')
    result = session.expect(['Password:'])
    if result != 0:
         print ("fail on ", ip)
         exit()
    session.sendline(enable)
    if result != 0:
        print ("fail on ", ip)
        exit()
    print('show ip completed')
    
    session.sendline('sh run | i hostname')
    result = session.expect
    if result == 0:
        print ('Command sent ok')
    elif result == 1:
        print ('Timed out.')
    elif result == 2:
        print ('EOF')
    show_output = session.before
    session.close
##  gather command output and save somehow
    device_list.append(device_info[0])
    print ('Router ', show_output)
