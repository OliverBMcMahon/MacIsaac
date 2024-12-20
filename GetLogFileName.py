#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:02:14 2024

@author: oliver
"""
from datetime import datetime

def CreateLogfilename():
    now = datetime.now()
    
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    time = time.replace(":","_")
    logfilename = "Log_%s_%s_%s_%s.log" %(year, month, day, time)
    print(logfilename)
    return logfilename	