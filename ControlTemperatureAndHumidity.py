import socket
import sqlite3
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('169.254.168.139', 23))

msg = 'hello'
s.send(msg.encode())
msg = s.recv(1024)
print( msg.decode("utf-8"))
words = msg.decode("utf-8").split(',')
print(words[0].strip())
print(words[1].strip())
nowstr = datetime.now().strftime('%Y/%m/%d/%H/%M')
print(nowstr)


    
           