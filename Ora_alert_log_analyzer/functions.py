#!/usr/bin/env python

import subprocess
import sys
import datetime
import random

__version__ = "0.1"


months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
years=[datetime.date.today().strftime("%Y"),(datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y"),(datetime.datetime.now() - datetime.timedelta(days=2*365)).strftime("%Y")]


def watch_door():
    import alert
    print "\n"
    print "Welcome to Alert log analyzer. Please select:\n"
    print " Press 1. Too see alert history in one month period, example: Feb 2015 or Jan 2014"
    print " Press 2. For all ORA errors display"
    print " Press 3. For particular ORA error, example: ORA-00600\n"
    alert.selection=raw_input('Select 1 or 2 :')
    if  alert.selection == str(1):
           print "Too see alert history in one month period provide date, example: Feb 2015 or Jan 2014\n"
           input = raw_input('Insert date :  ')
           alert.sys.argv=input.split()

    elif alert.selection == str(2):
           print "Too see ORA errors history prass enter"

    elif alert.selection == str(3):
           print "Please type ORA error"
           ora_err = raw_input('Insert ORA-xxx error :  ')
           alert.ora_err=ora_err



def watch_first_para():
    import alert
    if (alert.month not in months) or (alert.year not in years):
           print "You did not entered two parameters on the input or data is incorrect, try again"
           sys.exit()
    if len(alert.sys.argv) == 0 or len(alert.sys.argv) == 1:
        print "You forgot to enter parameters, please try again"
        sys.exit()

def watch_path():
    result=subprocess.Popen(['ls $ORACLE_BASE/diag/rdbms/*/$ORACLE_SID/trace/alert_$ORACLE_SID*.log'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.wait()
    print result.returncode

    if result.returncode !=0:
         print "Problem with the alert log file"
         print result.communicate()[1],
         sys.exit()
    else:
         print "Alert log file has been found"



def watch_first_alert():
    import alert

    if  alert.selection == str(1):

        cmd="head -10000 $ORACLE_BASE/diag/rdbms/*/$ORACLE_SID/trace/alert_$ORACLE_SID*.log | awk '/"+alert.year+"/{x=NR+6}(NR<=x){print}'| awk '/"+alert.month+"/{x=NR+6}(NR<=x){print}'"
        print cmd

    elif alert.selection == str(2):
        cmd="head -10000 $ORACLE_BASE/diag/rdbms/*/$ORACLE_SID/trace/alert_$ORACLE_SID*.log | awk '/ORA-/{x=NR+6}(NR<=x){print}'"

    elif alert.selection == str(3):
        cmd="head -10000 $ORACLE_BASE/diag/rdbms/*/$ORACLE_SID/trace/alert_$ORACLE_SID*.log | awk '/"+alert.ora_err+"/{x=NR+6}(NR<=x){print}'"


    storage=[]
    grepped=[]
    result=subprocess.Popen([cmd],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in result.stdout:
        grepped.append(i)
#        print grepped
#-----------------------------------------------
# delete new line (\n) from the table
#-----------------------------------------------

    storage[:] = [line.rstrip('\n') for line in grepped]

    space=0
    for i in storage:
        print i
        space +=1
#        if space%4==0:
#            print "--------------------------------"
