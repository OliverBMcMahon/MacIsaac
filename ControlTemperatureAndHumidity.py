# -*- coding: utf-8 -*-
import sqlite3
import time
import MonitorClass
import RelayControl
import MyLogger as logger
import MonitorTemperatureAndHumidity
import CreateLogfilename as clf
import UtilityFunctions as ufcn
from datetime import datetime
from configparser import ConfigParser

# Global variables
iniFile = 'MacIsaac.ini'

# Get most recent reports from database.
def GetReports():
    reports = []
    logger.logInfoMsg("GetReports()")
    dbname = ufcn.GetDatabaseName(iniFile)
    monitors = ufcn.GetMonitors(iniFile)   
    for monitor in monitors:
        try:
            conn = sqlite3.connect(dbname)
            cursor = conn.cursor()
            name = monitor.name
            cmd = f'''SELECT * FROM reports 
                WHERE monitor LIKE '{name}'
                ORDER BY datetime DESC LIMIT 1;'''
            cursor.execute(cmd)
            newrpt = cursor.fetchall() 
            reports.append(newrpt)
            print(newrpt)
        except Exception as e:
            print(e)
        finally:
            conn.close()     
    return reports
    
# Begin application code ------------------------------------------
def main():
    # Get unique nasme for logfile.
    logfile = clf.CreateLogfilename("CONTROL")
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
            reports = GetReports()
            # Reset interval start time.
            t1 = datetime.now()
            # SetRelays with envReports.
            RelayControl.SetRelays(reports)        
   
# Run main() if this file is being run directly       
if __name__ == '__main__':
    main()






    
           