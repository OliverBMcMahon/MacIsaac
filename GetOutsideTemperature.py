# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:01:32 2024

@author: mcmah

This module is run stand-alone.
It preiodically gets the outside temperature and humidity from google. 
It then writes the time, temperature and humidity to the OUTSIDE 
table in the GymTest database.
"""
import requests
import sqlite3
import socket
import MyLogger as logger
import UtilityFunctions as ufcn
import CreateLogfilename as clf
from datetime import datetime
from bs4 import BeautifulSoup

# Global variables
iniFile = 'MacIsaac.ini'

def GetMonitor(iniFile):
    dbname = ufcn.GetDatabaseName(iniFile)
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        # 'CEILING' will be changed to 'OUTSIDE' for production.
        cmd = "SELECT * FROM monitors WHERE name LIKE 'CEILING';"
        cursor.execute(cmd)
        output = cursor.fetchall()      
        for sublist in output:
            name = sublist[0]
            ip = sublist[2]
            port = sublist[3]
    except sqlite3.Error as e:
        # Handle the exception
        logger.logErrorMsg(f"An sqlite error occurred: {e}")
    finally:
        conn.close()
    return name, ip, port

# This fcn gets outside temperature from google. 
def GetGoogleOutsideTemperature():
    # Enter city name
    city = "harvard, ma"

    # Creating URL and making requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    # Getting raw data using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    #hum = = soup.find("span", attrs={"id": "wob_hm"}).text
    return temp

def GetOutsideReport(name, ip, port):
    # Create socket to connect to Arduino monitor.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))               
    hello = '123'
    s.send(hello.encode())    
    msg = s.recv(1024)

    humidity = ufcn.GetHumidityFromMonitorMessage(msg)
    temperature = ufcn.GetTemperatureFromMonitorMessage(msg)
    now = datetime.now()  
    try:
        dbname = ufcn.GetDatabaseName(iniFile)
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cmdstr = "INSERT INTO weather (datetime, temperature, humidity) VALUES(?, ?, ?);"
        cursor.execute((cmdstr),(now, temperature, humidity))
        conn.commit()
    except socket.error as err:
        logger.logErrorMsg(err)
    finally:
        conn.close()    

if __name__ == '__main__':
    # Get unique nasme for logfile.
    logfile = clf.CreateLogfilename("OUTSIDE")
    # Send log filename to logger.
    logger.assignLogfilename(logfile)
    logger.logInfoMsg("Begin new run.")
    
    outsideInfo = GetMonitor(iniFile)
    print(outsideInfo)
    name = outsideInfo[0]
    ip = outsideInfo[1]
    port = outsideInfo[2]
    
    # Get initial time for polling interval.
    intervalMinutes = 1
    t1 = datetime.now()
    elapsed = 0
    while True:
        t2 = datetime.now()
        elapsed = t2 - t1
        if elapsed.seconds/60 >= float(intervalMinutes):
            GetOutsideReport(name, ip, port)
            # Update Arduino's interval start time.
            t1 = datetime.now()