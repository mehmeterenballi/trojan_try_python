#server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  #this is your computer's default ip. it will be server ip
port = 1234

server.bind((host, port))  #bind server
server.listen(5)

run = True
client, addr = server.accept()
print('Got Connection from ', addr)

while run:
    try:
        data = input('>>>')
        client.send(data.encode('UTF-8'))  #send data to client

        msg=client.recv(1024)
        print(msg.decode('UTF-8'))
    except ConnectResetError:
        print('Client Lost. Trying to connect...')
        client, addr = server.accept()
        print('Got Connection from ',addr)
