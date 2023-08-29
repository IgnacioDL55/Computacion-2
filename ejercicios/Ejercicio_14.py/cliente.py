import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 50011))

while True:
    data = input()
    s.send(data.encode())
    if data == 'exit':
        break
