#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:48:45 2024

@author: oliver
"""
import sqlite3

def CreateDatabaseAndTables():
    try:
        conn = sqlite3.connect("GymTest.db")
        cursor = conn.cursor()
        # Create the mpnitors table.
        cmdstr = '''CREATE TABLE IF NOT EXISTS reports(
                        datetime INT,
                        monitor TEXT NOT NULL,
                        temperature REAL,
                        humidity REAL);'''
        cursor.execute(cmdstr)
        conn.commit()
        
        # Create the reports table.
        cmdstr = '''CREATE TABLE IF NOT EXISTS monitors(
                        name TEXT NOT NULL,
                        mac TEXT,
                        IP TEXT,
                        port INTEGER);'''
        cursor.execute(cmdstr)
        conn.commit()
        
        # Create the relays table.
        cmdstr = '''CREATE TABLE IF NOT EXISTS relays(
                        name TEXT NOT NULL,
                        datetime INT,
                        state TEXT);'''
        cursor.execute(cmdstr)
        conn.commit()
        
        # Create the weather table.
        cmdstr = '''CREATE TABLE IF NOT EXISTS weather(
                        datetime INT,
                        temperature REAL,
                        humidity REAL);'''
        cursor.execute(cmdstr)
        conn.commit()
        
        # Insert as row for each monitor being used.
        name1 = 'CEILING'
        mac1 = "A8:61:0A:0F:1A:AA"
        ip1 = "192.168.40.139"
        port = 23     
        cmdstr = "INSERT INTO monitors (name, mac, IP, port) VALUES(?, ?, ?, ?);"
        cursor.execute(cmdstr, (name1, mac1, ip1, port))
        conn.commit()
        
    except Exception as err:
        print("sqlite3 error: ", err)
    finally:
        conn.close()
        
# Run main() if this file is being run directly       
if __name__ == '__main__':
    CreateDatabaseAndTables()
