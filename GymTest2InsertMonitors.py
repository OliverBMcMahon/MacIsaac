#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:48:45 2024

@author: oliver
"""

import sqlite3

conn = sqlite3.connect("GymTest2.db")

cursor = conn.cursor()

name1 = 'Monitor1'
mac1 = "A8:61:0A:0F:1A:AA"
ip1 = "169.254.168.139"

name2 = 'Monitor2'
mac2 = "A8:61:0A:AE:)D:AC"
ip2 = "169.254.168.140"
port = 23

cmdstr = "INSERT INTO monitors (name, mac, IP, port) VALUES(?, ?, ?, ?);"

cursor.execute(cmdstr, (name1, mac1, ip1, port))
cursor.execute(cmdstr, (name2, mac2, ip2, port))

conn.commit()
conn.close()

