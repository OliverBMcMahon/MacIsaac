import socket
import sqlite3
from datetime import datetime

# Define functions that will be used in the code which follows
# MonitorMessage is the row of data returned from themonitors table
def GetTemperatureFromMonitorMessage(msg):
    words = msg.decode("utf-8").split(',')
    temperature = float(words[1].strip())
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

    cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
    cursor.execute((cmdstr),(nowstr, name, temperature, humidity))

    conn.commit()
    conn.close()
    
def GetMonitors():
    conn = sqlite3.connect("GymTest2.db")
    cursor = conn.cursor()
    cmd = "SELECT * FROM monitors;"
    cursor.execute(cmd)
    output = cursor.fetchall() 
    return output

def GetMonitorName(monitor_row):
    words = monitor_row.split(',')
    print(words)

# Begin application code ------------------------------------------

# Connect to databse 
conn = sqlite3.connect("GymTest2.db")
cursor = conn.cursor()

monitors = GetMonitors()
# When we have 2 monitors running we will implement this loop
#for monitor in monitors:
#        monitor = monitors[0]
#        ip = monitor[2]
#        port = monitor[3]

monitor = monitors[0]
name = monitor[0]
ip = monitor[2]
port = monitor[3]

print(name + " " + ip)

GetMonitorReport(name, ip, port)



    
           