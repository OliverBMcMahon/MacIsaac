#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:41:46 2024

@author: oliver
"""

import sqlite3

conn = sqlite3.connect("GymTest.db")
cursor = conn.cursor()


cmdstr = '''CREATE TABLE IF NOT EXISTS reports
            (
                datetime TEXT,
                monitor TEXT NOT NULL,
                temperature REAL,
                humidity REA);'''

cursor.execute(cmdstr)

cmdstr = '''CREATE TABLE IF NOT EXISTS monitors
            (
                name TEXT NOT NULL,
                mac TEXT,
                IP TEXT,
                port INTEGER);'''

cursor.execute(cmdstr)

conn.commit()
conn.close()

