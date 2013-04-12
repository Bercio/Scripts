#!/bin/sh
if grep -q up /sys/class/net/wlp3s0/operstate ||  grep -q up /sys/class/net/enp4s0/operstate; then
    nowEvent=`gcalcli --configFolder /home/bercio/.config/gcalcli agenda | head -2 |tail -1|cut -f8- -d' '`
    nextEvent=`gcalcli --nostarted --configFolder /home/bercio/.config/gcalcli agenda | head -2 |tail -1|cut -f6- -d' '`
    echo "$nowEvent | $nextEvent" >| /tmp/gcalcache
    exit 0
else
    echo "No Data\n" >| /tmp/gcalcache
fi

