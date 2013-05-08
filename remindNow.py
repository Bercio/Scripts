#!/usr/bin/env python

"""
Display the current and the next event from remind
"""
import time
import subprocess
remindFile = '/home/bercio/Reminders/all.rem'
def getCalendar():
    remindOutput = subprocess.check_output(['remind', '-s+1' '-b1', remindFile])
    lsRemindOutput =  for i in remindOutput.splitlines():
                            i = i.split()

    shreddedRemindOutput = []
    for i in lsRemindOutput:
        if i[0] == time.strftime("%Y/%m/%d", time.localtime()):
            shreddedRemindOutput += i
    return shreddedRemindOutput
def getEvents():
    startandEndTimes = getCalendar()[5].strip(':').split('-')
    for i, v in enumerate(getCalendar()):
        if startandEndTimes[0] <= time.strftime("%H%M") <= startandEndTimes[1]:
            eventNow = v
            eventThen = getCalendat[(i+1)]
            return (eventNow, eventNow)
            exit
        else:
            return "Nothing else today"
print(getEvents())

