#!/usr/bin/env python

"""
Display the current and the next event from remind
"""
import time
import subprocess
remindFile = '/home/bercio/Reminders/all.rem'

def getDayEvents():
    remindOutput = subprocess.check_output(['remind', '-s+1' '-b1', remindFile]).splitlines()
    dayEvents = []
    for lines in remindOutput:
        lines = lines.split()
        if lines[0] == time.strftime("%Y/%m/%d"):
            dayEvents.append(lines)
    return dayEvents

for lines in getDayEvents():
    #split  the field starttime-sendtime in the fields start-time and endtime.
    lines[5].split('-')
    lines.insert(5, lines[5][0])
    lines[5] = lines[5][1]
    if time.strptime(','.join(lines[0], lines[4])) < time.localtime() < time.strptime(''.join(lines[0], lines[5])):
        nowEvent = lines
        nextEvent = getDayEvents()[(getDayEvents().index(lines) + 1)]
        exit
print(nowEvent[6:-1], "|", nextEvent[6:-1])
