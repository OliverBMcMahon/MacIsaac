#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:02:14 2024

@author: oliver
"""
import os
from datetime import datetime

def CreateLogfilename():
    path = os.path.abspath(os.getcwd())
    path += "\\Log"
   
    if not os.path.exists(path):
        os.makedirs(path)
       
    now = datetime.now()  
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    time = time.replace(":","_")
    logfilename = "%s\\Log_%s_%s_%s_%s.log" %(path, year, month, day, time)
    print(logfilename)
    return logfilename

if __name__ == "__main__":
    name = CreateLogfilename()
   