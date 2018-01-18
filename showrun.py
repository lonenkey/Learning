#python 3.5.2
import pexpect

device_list = list()
device_info = {}
file = open('devices.txt','r')
for device in file:
    device_info=device.split(',')
    print (device_info)
    ip = device_info[0]
    username = device_info[1]
    password = device_info[2]
    enable   = device_info[3]
##  connect session and send commands
##  gather command output and save somehow
    device_list.append(device_info[0])

print(device_list)
