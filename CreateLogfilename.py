# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 06:35:45 2024

@author: mcmah
"""


import os
from datetime import datetime

def CreateLogfilename():
    path = os.path.abspath(os.getcwd())
    path += "/Logs"
   
    if not os.path.exists(path):
        # Create the folder.
        os.makedirs(path)
       
    now = datetime.now()  
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    time = time.replace(":","_")
    logfilename = "%s/Log_%s_%s_%s_%s.log" %(path, year, month, day, time)
    print(logfilename)
    return logfilename

if __name__ == "__main__":
    name = CreateLogfilename()
