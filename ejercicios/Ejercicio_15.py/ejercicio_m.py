import socket
import multiprocessing
import sys

def process_client(connection, address):
    print("Proceso lanzado de", address)
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print("Recibido:", message, "de", address)
            if message.lower() == "exit":
                break
            response = message.upper() + "\r\n"
            connection.sendall(response.encode())

    print("Cerrando conexion de", address)

def main():
    host = ""
    port = 50011 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("El servidor esta escuchando del puerto:", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexion", client_address)
        process = multiprocessing.Process(target=process_client, args=(client_socket, client_address))
        process.start()

if __name__ == "__main__":
    main()
