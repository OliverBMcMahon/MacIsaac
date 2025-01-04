# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:54:56 2024

@author: mcmah
"""
import sqlite3
import MyLogger as logger
import MonitorClass
from configparser import ConfigParser

# msg is the row of data returned from the monitors table
def GetTemperatureFromMonitorMessage(msg):
    words = msg.decode("utf-8").split(',')
    temperature = float(words[1].strip()) 
    temperature = temperature * 1.8 + 32.0
    return temperature

def GetHumidityFromMonitorMessage(msg):
    words = msg.decode("utf-8").split(',')
    humidity = float(words[0].strip())
    return humidity

def GetDatabaseName(iniFile):
    try:
        config = ConfigParser() 
        config.read(iniFile)
        name = config["DATABASE"]["dbname"]
    except IOError as err:
        logger.logErrorMsg(err)
    return name
    
def GetMonitors(iniFile):
    dbname = GetDatabaseName(iniFile)
    monitor_list = []
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cmd = "SELECT * FROM monitors;"
        cursor.execute(cmd)
        output = cursor.fetchall() 
        
        for sublist in output:
            name = sublist[0]
            mac = sublist[1]
            ip = sublist[2]
            port = sublist[3]
            mon = MonitorClass.Monitor(name, mac, ip, port)
            monitor_list.append(mon)
    except sqlite3.Error as e:
        # Handle the exception
        logger.logErrorMsg(f"An sqlite error occurred: {e}")
    finally:
        conn.close()
    return monitor_list

def GetMonitorNames(dbname):
    monitor_names = []
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cmd = "SELECT * FROM monitors;"
        cursor.execute(cmd)
        output = cursor.fetchall() 
        
        for sublist in output:
            name = sublist[0]
            monitor_names.append(name)
    except sqlite3.Error as e:
        # Handle the exception
        logger.logErrorMsg(f"An sqlite error occurred: {e}")
    finally:
        conn.close()
    return monitor_names