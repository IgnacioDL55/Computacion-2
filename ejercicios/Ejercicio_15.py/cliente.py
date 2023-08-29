import socket

def main():
    host = "localhost"
    port = 50011

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = input("Mensaje: ")
            client_socket.sendall(message.encode())
            
            if message.lower() == "exit":
                break
            
            response = client_socket.recv(1024)
            print("Respuesta", response.decode())
    except KeyboardInterrupt:
        print("\nCerrando cliente.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
