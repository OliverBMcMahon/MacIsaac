import socket
import sqlite3
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('169.254.168.139', 23))

conn = sqlite3.connect("GymTest2.db")

cursor = conn.cursor()

msg = 'hello'
s.send(msg.encode())
msg = s.recv(1024)
print( msg.decode("utf-8"))
words = msg.decode("utf-8").split(',')

name = 'monitor1'
humidity = float(words[0].strip())
temperature = float(words[1].strip())
nowstr = datetime.now().strftime('%Y/%m/%d/%H/%M')
print(nowstr)

cmdstr = "INSERT INTO reports (datetime, monitor, temperature, humidity) VALUES(?, ?, ?, ?);"
cursor.execute((cmdstr),(nowstr, name, temperature, humidity))
rows = cursor.fetchall()

conn.commit()
conn.close()


    
           