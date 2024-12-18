import socket
import sqlite3
import time
from datetime import datetime
from configparser import ConfigParser

# Define functions that will be used
# msg is the row of data returned from the monitors table
def GetTemperatureFromMonitorMessage(msg):
    words = msg.decode("utf-8").split(',')
    temperature = float(words[1].strip()) 
    print(temperature)
    temperature = temperature * 1.8 + 32.0
    print(temperature)
    return temperature

def GetHumidityFromMonitorMessage(msg):
    words = msg.decode("utf-8").split(',')
    humidity = float(words[0].strip())
    return humidity

def GetMonitorReport(name, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
            
    hello = 'bah'
    s.send(hello.encode())
    
    msg = s.recv(1024)
    print( msg.decode("utf-8"))

    humidity = GetHumidityFromMonitorMessage(msg)
    temperature = GetTemperatureFromMonitorMessage(msg)
    nowstr = datetime.now().strftime('%Y/%m/%d/%H/%M')
    print(nowstr)

    config = ConfigParser() # Get dbname
    config.read('MacIsaac.ini')
    dbname = config["DATABASE"]["dbname"]
    
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
    cursor.execute((cmdstr),(nowstr, name, temperature, humidity))

    conn.commit()
    conn.close()
    
def GetMonitors(dbFileName):
    conn = sqlite3.connect(dbFileName)
    cursor = conn.cursor()
    cmd = "SELECT * FROM monitors;"
    cursor.execute(cmd)
    output = cursor.fetchall() 
    conn.close()
    return output

def GetMonitorName(monitor_row):
    words = monitor_row.split(',')
    print(words)

def GetReports():
    # Get config file parameters
    config = ConfigParser()
    config.read('MacIsaac.ini')
    dbname = config["DATABASE"]["dbname"]
    # Get list of monitors
    monitors = GetMonitors(dbname)
    # Extract parameters for monitor1
    for monitor in monitors:
           name = monitor[0]
           ip = monitor[2]
           port = int(monitor[3])
           # Show monitor name and ip address
           print(name + " " + ip)
           GetMonitorReport(name, ip, port)
           
    
# Begin application code ------------------------------------------
def main():
    # Setup for timer interval loop
    # Get config file parameters
    config = ConfigParser()
    config.read('MacIsaac.ini')
    intervalMinutes = config["TIMER"]["interval"]
    t1 = datetime.now()
    elapsed = 0
    while True:
        t2 = datetime.now()
        elapsed = t2 - t1
        if elapsed.seconds/60 >= float(intervalMinutes):
            GetReports()
            t1 = datetime.now()
        
if __name__ == '__main__':
    main()






    
           