#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:32:26 2024

@author: oliver
"""

import sqlite3

def GetMonitors():
    conn = sqlite3.connect("GymTest2.db")
    cursor = conn.cursor()
    cmd = "SELECT * FROM monitors;"
    cursor.execute(cmd)
    output = cursor.fetchall() 
    return output

def GetMonitorName(monitor_row):
    words = monitor_row.split(',')
    print(words)
  
