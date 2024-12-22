# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:22:41 2024

@author: mcmah
"""
# Functions for writing messages to log file.
from datetime import datetime

# Globals
fname = ""

# assignLogfilename must be called before any other calls.
def assignLogfilename(filename):
    global fname
    fname = filename

def log_msg(msg):
    with open(fname, 'a') as logfile:
        logfile.write(msg)
       
def logInfoMsg(msg):
    time = getTimeStr()
    fmtstr = "%s::INFO--> %s\n" %(time, msg)
    log_msg(fmtstr)

def logDebugMsg(msg):
    time = getTimeStr()
    fmtstr = "%s::DEBUG--> %s\n" %(time, msg)
    log_msg(fmtstr)

def logWarnMsg(msg):
    time = getTimeStr()
    fmtstr = "%s::WARN--> %s\n" %(time, msg)
    log_msg(fmtstr)

def logErrorMsg(msg):
    time = getTimeStr()
    fmtstr = "%s::ERROR--> %s\n" %(time, msg)
    log_msg(fmtstr)

def logFailMsg(msg):
    time = getTimeStr()
    fmtstr = "%s::FAIL--> %s\n" %(time, msg)
    log_msg(fmtstr)
   
def getTimeStr():
    now = datetime.now()
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    timestr = "%s-%s-%s %s" %(year, month, day, time)
    return timestr
   
if __name__ == "__main__":
    logInfoMsg("INFO message")
    logDebugMsg("DEBUG message")
    logWarnMsg("WARN message")
    logErrorMsg("ERROR message")
    logFailMsg("FAIL message")
