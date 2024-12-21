# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 06:35:45 2024

@author: mcmah
"""


import os
from datetime import datetime

def CreateLogfilename():
    # Get a unique name for log file.
    path = os.path.abspath(os.getcwd())
    path += "\\Logs"
    # Create Logs folder, if it doesn't exist.
    if not os.path.exists(path):
        os.makedirs(path)
    # Put date and time in filename.   
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
