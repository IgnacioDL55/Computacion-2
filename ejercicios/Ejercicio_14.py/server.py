import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 50011))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        
        while True:
            data = conn.recv(1024)
            if data.decode() == 'exit':
                break
            else:
                print(data.decode())
            conn.sendall(data)
