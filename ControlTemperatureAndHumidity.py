# -*- coding: utf-8 -*-
import socket
import sqlite3
import logging
import MonitorClass
import GetLogFileName
from datetime import datetime
import UtilityFunctions as ufcn
import EnvironmentReportClass as erc
from configparser import ConfigParser

# Global variables
envRports = []
iniFile = 'MacIsaac.ini'
dbname = ufcn.GetDatabaseName(iniFile)
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logfilename = GetLogFileName.CreateLogfilename()

# Functions 
def GetMonitorReport(name, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
            
    hello = 'bah'
    s.send(hello.encode())    
    msg = s.recv(1024)

    humidity = ufcn.GetHumidityFromMonitorMessage(msg)
    temperature = ufcn.GetTemperatureFromMonitorMessage(msg)
    
    rpt = erc.EnvironmentReport(name, temperature, humidity)

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
    cursor.execute((cmdstr),(rpt.rpttime, name, temperature, humidity))
    conn.commit()
    conn.close()    
    return rpt
    

def GetReports():
    global envRports
    envRports.clear() # We clear list because we only want 1 report per monitor.
    monitors = ufcn.GetMonitors(dbname)
    for monitor in monitors:
        newrpt = GetMonitorReport(monitor.name, monitor.ip, monitor.port)
        print(monitor.name, monitor.ip, monitor.port)
        envRports.append(newrpt)
    return envRports
    
# Begin application code ------------------------------------------
def main():
    logging.basicConfig(filename = logfilename, level = logging.DEBUG, format = LOG_FORMAT, filemode= 'w') 
    logger = logging.getLogger()
    logger.debug("Begin new run.")
    
    # Setup for timer interval loop
    # Get config file parameters
    config = ConfigParser()
    config.read('MacIsaac.ini')
    intervalMinutes = config["TIMER"]["interval"]
    t1 = datetime.now()
    elapsed = 0
    global envRports
    while True:
        t2 = datetime.now()
        elapsed = t2 - t1
        if elapsed.seconds/60 >= float(intervalMinutes):
            envRports = GetReports()
            t1 = datetime.now()
   
# Run main() if this file is being run directly       
if __name__ == '__main__':
    main()






    
           