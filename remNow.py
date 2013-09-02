#!/usr/bin/env python
from time import *
from subprocess import *
REMFILE = ""
events = str(check_output(["rem", "-s+1", "-b1"]))
# the [:-1] eliminates wierdnon-unicode formatting
events_lines = events.split("\\n")[:-1]
fields = []
for line in events_lines:
    fields.append(line.split())
#eliminates wierdnon-unicode formatting
fields[0][0] = fields[0][0][2:]
#transform interval start-end in two fields start, end
for lines in fields:
    lines[5] = lines[5].split("-")

for i, lines in enumerate(fields):
    if len(fields[i][5][1]) > 5:
            fields[i][5][1] = fields[i][5][1][:5]
            fields[i][0] = fields[i][0][:-2] + str(int(fields[i][0][8:]) + 1)
    start =  strptime((fields[i][0] + fields[i][5][0]), "%Y/%m/%d%H:%M")
    end = strptime((fields[i][0] + fields[i][5][1]), "%Y/%m/%d%H:%M")
    if start <= localtime() <= end:
        inow = i
        now = lines
        break
try:
    then = fields[(inow + 1)]
    print(" ".join(now[6:-2]))
    print(" ".join(then[6:]))
except NameError:
    print("No Events\nAt all")
