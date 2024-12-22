# -*- coding: utf-8 -*-
import socket
import sqlite3
import MyLogger as logger
import MonitorClass
#import RelayControl
import CreateLogfilename as clf
import UtilityFunctions as ufcn
import EnvironmentReportClass as erc
from datetime import datetime
from configparser import ConfigParser

# Global variables
iniFile = 'MacIsaac.ini'

# Functions 
def GetMonitorReport(name, ip, port):
    try:
        # Create socket to connect to Arduino monitor.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))               
        hello = 'bah'
        s.send(hello.encode())    
        msg = s.recv(1024)
    
        humidity = ufcn.GetHumidityFromMonitorMessage(msg)
        temperature = ufcn.GetTemperatureFromMonitorMessage(msg)
        
        rpt = erc.EnvironmentReport(name, temperature, humidity)
    
        dbname = ufcn.GetDatabaseName(iniFile)
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
        cursor.execute((cmdstr),(rpt.rpttime, name, temperature, humidity))
        conn.commit()
    except socket.error as err:
        logger.logErrorMsg(err)
    finally:
        conn.close()    
    return rpt
    

def GetReports():
    envReports = []
    logger.logInfoMsg("GetReports()")
    monitors = ufcn.GetMonitors(iniFile)
    for monitor in monitors:
        newrpt = GetMonitorReport(monitor.name, monitor.ip, monitor.port)
        logger.logInfoMsg(f"{monitor.name} {monitor.ip} {monitor.port}")
        envReports.append(newrpt)
    return envReports
    
# Begin application code ------------------------------------------
def main():
    # Get unique nasme for logfile.
    logfile = clf.CreateLogfilename()
    # Send log filename to logger.
    logger.assignLogfilename(logfile)
    logger.logInfoMsg("Begin new run.")
    
    # Setup for timer interval loop
    # Get config file parameters
    config = ConfigParser()
    config.read('MacIsaac.ini')
    intervalMinutes = config["TIMER"]["interval"]
    # t1 is start time for Arduino's interval.
    t1 = datetime.now()
    elapsed = 0
    while True:
        t2 = datetime.now()
        elapsed = t2 - t1
        if elapsed.seconds/60 >= float(intervalMinutes):
            envReports = GetReports()
            # Update Arduino's interval start time.
            t1 = datetime.now()
        # Call SetRelays with envReports.
        #RelayControl.SetRelays(envReports)        
   
# Run main() if this file is being run directly       
if __name__ == '__main__':
    main()






    
           