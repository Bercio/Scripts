#!/usr/bin/env python
#TODO= use tempfile module, safer
#TODO= make it into a daemon
from subprocess import call
#find out how the battery is doing
def batteryCharge():
    fullChargeFile = open("/sys/class/power_supply/BAT0/charge_full", 'r')
    nowChargeFile = open("/sys/class/power_supply/BAT0/charge_now", 'r')
    fullCharge = int(fullChargeFile.readline())
    nowCharge = int(nowChargeFile.readline())
    percentageNowCharge = 100*nowCharge//fullCharge
    return percentageNowCharge
def batteryStatus():
    statusFile = open("/sys/class/power_supply/BAT0/status", 'r')
    status = statusFile.readline()
    return status
def alreadyNotified(condition):
    try:
        with open("".join(["/tmp/", condition])):
            return True
    except IOError:
        return False
def notify():
    if batteryCharge() <= 10 and batteryStatus() == "Discharging\n" and not alreadyNotified("batIll"):
        call("""echo "naughty.notify({title = 'Battery', text = 'Battery low! Plug or pray',height= 100, width = 300, timeout = 5})" | awesome-client -""", shell=True)
        open("/tmp/ill", "w+")
    elif batteryCharge() == 0 and batteryStatus() == "Discharging\n" and not alreadyNotified("batDead"):
        call("""echo "naughty.notify({title = 'Battery', text = 'Battery dieing! Plug or die', bg = '#ad1313', fg = '#222680', height= 100, width = 300, timeout = 5})" | awesome-client -""", shell=True)
        open("/tmp/batDead", "w+")
if __name__ == "__main__":
    notify()
