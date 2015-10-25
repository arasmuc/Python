#!/usr/bin/env python

import functions
import subprocess
import sys
import datetime

selection = 0
ora_err = "ORA"

print __name__

functions.watch_door()


if selection == str(1):
    lenght=len(sys.argv)
    month=str(sys.argv[0])
    year=str(sys.argv[1])

# functions to check input
    functions.watch_first_para()

# check if Alert Log file exists and path is correct
    functions.watch_path()

# search ORA errors in alerts log
    functions.watch_first_alert()
    sys.exit()


elif selection == str(2):
    print "TUTAJ"
    functions.watch_first_alert()
    sys.exit()


elif selection == str(3):
    print "TRZECIA"
    functions.watch_first_alert()
    sys.exit()

