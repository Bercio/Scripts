#!/usr/bin/env python
import subprocess
import os
import tempfile
import time

def batteryStatus():
    statusFile = open("/sys/class/power_supply/BAT0/status", 'r')
    status = statusFile.readline()
    if status == "Charging\n":
        status = "⚡"
    elif status == "Discharging\n":
        status = "⌁"
    else:
        status = ""
    return status
def batteryRemainingTime():
    ibam = subprocess.getoutput("ibam --batteryadaptive").split()
<<<<<<< HEAD
    #ibam output is different wether the bat is chargin or discharging, if
    #charging Adapted bat time left is first line, else is last
    if ibam[0] == "Adapted":
        ibam = ibam[4]
    else:
        ibam = ibam[-1]
    ibam = time.strptime(ibam, "%H:%M:%S")
    return ibam
def iscritical():
    if batteryRemainingTime() < time.strptime("00:05:00", "%H:%M:%S"):
        for f in os.listdir("/tmp"):
            if f.endswith(".pybat"):
                return False
                exit
            else:
                return True
    else:
        #check if battery as recharged and deletes batpy files that flag it as
        #critical
        for f in os.listdir("/tmp"):
            if f.endswith(".pybat"):
                os.remove(''.join(("/tmp/",f)))
                exit
        return False
=======
    ibam = ibam[-1]
    ibam = time.strptime(ibam, "%H:%M:%S")
    return ibam
def iscritical():
    if batteryRemainingTime() <= time.gmtime(300):
        for f in os.listdir("/tmp"):
            if f.endswith(".pybat"):
                return True
                exit
if iscritical():
    subprocess.call(["notify-send, 'BATTERY', 'Bayyery low, you dig ?'"])
    tempfile.mkstemp(suffix='.pybat')

>>>>>>> 466cff6a76d33c90dd267ca7bbcdca9126a2e312
print(batteryStatus(),time.strftime("%H:%M", batteryRemainingTime()))
