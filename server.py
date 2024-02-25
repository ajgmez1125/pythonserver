import socket
import sys
import argparse

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_address = ('localhost', 1000)
server.bind(serv_address)
server.listen(5)
while True:
    print("Waiting")
    client, address = server.accept()
    data = client.recv(2048)
    if client:
        print('connected')
        message = 'Server response'
        client.send(message.encode('utf-8'))
        if data:
            print('received data')
            print(str(data))