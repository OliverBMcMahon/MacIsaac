#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:41:25 2024

@author: oliver
"""

import schedule 
from datetime import datetime
import time 
  
def func(): 
    print(datetime.now()) 
  
schedule.every(1).minutes.do(func) 
  
while True: 
    schedule.run_pending() 
    time.sleep(1) 