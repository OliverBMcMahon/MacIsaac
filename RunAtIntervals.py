# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:28:15 2024

@author: mcmah
"""

import schedule
import time

def func():
    import ControlTemperatureAndHumidity
    
schedule.every(5).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)