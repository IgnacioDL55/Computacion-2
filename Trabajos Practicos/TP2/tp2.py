import argparse
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from socketserver import ForkingMixIn
from multiprocessing import Process, Pipe
from PIL import Image

#Pruebo si esta instalado la libreria Pillow,en caso de no estarlo,doy la opcion de instalarla
try:
    from PIL import Image
except ImportError:
    print("Error: Pillow no está instalado.")

    instalar_pillow = input("¿Deseas instalar Pillow? (S/N): ").strip().lower()
    if instalar_pillow == 's':
        try:
            import pip
            pip.main(['install', 'Pillow'])
            from PIL import Image  # Importo la libreria luego de instalar
        except Exception as e:
            print(f"Error al instalar Pillow: {e}")
            exit()
    else:
        print("Instalación cancelada. Se necesita Pillow para ejecutar el script.")
        exit()


class ImageProcessingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        archivo_imagen = '/home/nacho/Escritorio/Computacion 2/Computacion-2/Trabajos Practicos/TP2/lebron_wade.jpg' #Cambiar el path para que funcione
        imagen_procesada = self.procesar_imagen(archivo_imagen)
        # Guardo la imagen procesada en un archivo temporal
        temp_file = 'lebron_wade_grey.jpg'
        with open(temp_file, 'wb') as f:
            f.write(imagen_procesada)
        try:
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.send_header('Content-disposition', 'attachment; filename="imagen_procesada.jpg"')
            self.end_headers()
            with open(temp_file, 'rb') as f:
                self.wfile.write(f.read())
        except BrokenPipeError:
            print("Cierre de conexion forzada por el cliente")

    def procesar_imagen(self, archivo_entrada): #Creo el pipe para procesar la imagen
        print("Creando un pipe")
        parent_pipe, child_pipe = Pipe()
        p = Process(target=self.procesar_imagen_child, args=(archivo_entrada, child_pipe))
        p.start()
        imagen_procesada = parent_pipe.recv()
        p.join() #Bloqueo el servidor hasta que termine el procesamiento de la imagen
        return imagen_procesada

    def procesar_imagen_child(self, archivo_entrada, conn): #Utilizo el modulo PILLOW para modificar la escala de colores de la imagen
        print (f"Creando Hijo ID:{os.getpid()},estamos procesando la imagen")
        imagen = Image.open(archivo_entrada).convert('L')
        temp_file = 'temp.jpg'
        imagen.save(temp_file)
        with open(temp_file, 'rb') as f:
            imagen_procesada = f.read()
        conn.send(imagen_procesada)
        os.remove(temp_file)
        print("Proceso hijo terminado")

class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        if ':' in server_address[0]:                #Verifico si es IPV6,si no lo es verufuca que sea IPV4
            self.address_family = socket.AF_INET6
        else:
            self.address_family = socket.AF_INET
        super().__init__(server_address, RequestHandlerClass)

def run_server(ip, puerto):
    handler = ImageProcessingHandler
    server = ForkingHTTPServer((ip, puerto), handler)

    print(f"Servidor HTTP en http://{ip}:{puerto}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print(" Servidor detenido.")

def main():
    parser = argparse.ArgumentParser(description='Servidor HTTP concurrente para procesar imágenes')
    parser.add_argument('-i', '--ip',default='::', help='Dirección IP del servidor')
    parser.add_argument('-p', '--puerto', type=int, default=8000, help='Puerto del servidor')
    args = parser.parse_args()
    
    run_server(args.ip, args.puerto)

    #Ejemplo de uso: python3 tp2.py -i 127.0.0.1 -p 8080

if __name__ == '__main__':
    main()


