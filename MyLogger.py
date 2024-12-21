# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:22:41 2024

@author: mcmah
"""
# Functions for writing messages to log file.
from datetime import datetime

def log_msg(fname, msg):
    with open(fname, 'a') as logfile:
        logfile.write(msg)
       
def logInfoMsg(fname, msg):
    time = getTimeStr()
    fmtstr = "%s::INFO--> %s\n" %(time, msg)
    log_msg(fname, fmtstr)

def logDebugMsg(fname, msg):
    time = getTimeStr()
    fmtstr = "%s::DEBUG--> %s\n" %(time, msg)
    log_msg(fname, fmtstr)

def logWarnMsg(fname, msg):
    time = getTimeStr()
    fmtstr = "%s::WARN--> %s\n" %(time, msg)
    log_msg(fname, fmtstr)

def logErrorMsg(fname, msg):
    time = getTimeStr()
    fmtstr = "%s::ERROR--> %s\n" %(time, msg)
    log_msg(fname, fmtstr)

def logFailMsg(fname, msg):
    time = getTimeStr()
    fmtstr = "%s::FAIL--> %s\n" %(time, msg)
    log_msg(fname, fmtstr)
   
def getTimeStr():
    now = datetime.now()
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    timestr = "%s-%s-%s %s" %(year, month, day, time)
    return timestr
   
if __name__ == "__main__":
    logInfoMsg("log.file", "INFO message")
    logDbgMsg("log.file", "DEBUG message")
    logWarnMsg("log.file", "WARN message")
    logErrorMsg("log.file", "ERROR message")
    logFailMsg("log.file", "FAIL message")
