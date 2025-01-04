# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:54:56 2024

@author: mcmah

This module is run stand-alone.
It preiodically reads temperature and humidity from one or more
Arduino monitors. It then writes the time, monitorID, temperature and humidity
to a sqlite database.
"""
import socket
import sqlite3
import MyLogger as logger
import MonitorClass
import CreateLogfilename as clf
import UtilityFunctions as ufcn
from datetime import datetime
from configparser import ConfigParser

# Global variables
iniFile = 'Monitors.ini'

# Functions 
def GetMonitorReport(name, ip, port):
    msg = ""
    try:
        # Create socket to connect to Arduino monitor.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))               
        hello = '123'
        s.send(hello.encode())    
        msg = s.recv(1024)
        humidity = ufcn.GetHumidityFromMonitorMessage(msg)
        temperature = ufcn.GetTemperatureFromMonitorMessage(msg)
    except socket.error as err:
        print("GetMonitorReport error")
        print(ip)
        print(err)
        logger.logErrorMsg(err)   
        
    now = datetime.now()  
    dbname = ufcn.GetDatabaseName(iniFile)
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
        cursor.execute((cmdstr),(now, name, temperature, humidity))
        conn.commit()
    except Exception as err:
        logger.logErrorMsg(err)
        print(err)
    finally:
        conn.close()    

def GetReports():
    logger.logInfoMsg("GetReports()")
    monitors = ufcn.GetMonitors(iniFile)
    for monitor in monitors:
        GetMonitorReport(monitor.name, monitor.ip, monitor.port)
        logger.logInfoMsg(f"{monitor.name} {monitor.ip} {monitor.port}")
    
# Begin application code ------------------------------------------
def main():
    # Get unique nasme for logfile.
    logfile = clf.CreateLogfilename("MONITORS")
    # Send log filename to logger.
    logger.assignLogfilename(logfile)
    logger.logInfoMsg("Begin new run.")
    
    # Setup for timer interval loop
    # Get config file parameters
    config = ConfigParser()
    config.read(iniFile)
    intervalMinutes = config["TIMER"]["interval"]
    # t1 is start time for Arduino's interval.
    t1 = datetime.now()
    t1str = "Start new run: " + t1.strftime("%Y/%m/%d %H:%M:%S")
    elapsed = 0
    print(t1str )
    
    while True:
        t2 = datetime.now()
        elapsed = t2 - t1
        if elapsed.seconds/60 >= float(intervalMinutes):
            #GetReports()
            ip = "192.168.40.92"
            port = 23
            name = "CEILING"
            GetMonitorReport(name, ip, port)
            # Update Arduino's interval start time.
            t1 = datetime.now()
          
   
# Run main() if this file is being run directly       
if __name__ == '__main__':
    main()






    
           