#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:48:45 2024

@author: oliver
"""

import sqlite3
from datetime import datetime

conn = sqlite3.connect("GymTest2.db")

cursor = conn.cursor()
t = datetime.now()

time = datetime.now()
name = 'Monitor1'
temp = 75.01
hum = 47.5
cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"

rows = cursor.fetchall()

conn.commit()
conn.close()


print(t)

