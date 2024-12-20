# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:28:38 2024

@author: mcmah
"""
from datetime import datetime

class EnvironmentReport:
    
    def __init__(self, name, temperature, humidity):
        self.rpttime = datetime.now()
        self.name = name
        self.temperature = temperature
        self.hunidity =humidity