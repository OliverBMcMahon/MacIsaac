# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:54:56 2024

@author: mcmah
"""
import sqlite3
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
    config = ConfigParser() 
    config.read(iniFile)
    name = config["DATABASE"]["dbname"]
    print(name)
    return name
    
def GetMonitors(dbname):
    monitor_list = []
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cmd = "SELECT * FROM monitors;"
    cursor.execute(cmd)
    output = cursor.fetchall() 
    conn.close()
    for sublist in output:
        gmname = sublist[0]
        gmmac = sublist[1]
        gmip = sublist[2]
        gmport = sublist[3]
        mon = MonitorClass.Monitor(gmname, gmmac, gmip, gmport)
        monitor_list.append(mon)
    return monitor_list