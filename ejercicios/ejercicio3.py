#!/usr/bin/python3
#Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto.
#El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar.
#Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo.
#Esta última opción no debe ser obligatoria.
#Si hubiese errores deben guardarse en un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.

import argparse
import sys 

parse = argparse.ArgumentParser(description='contar numero de palabras y lineas del archivo')
parse.add_argument('archivo',type=str,help='nombre del archivo')
parse.add_argument('p',dest='promedio',action='store_true',help='imprimir el promedio de longiud de las palabras')

args = parse.parse_args()

try:
    with open(args.archivo, 'r') as archivo:
        contenido = archivo.read()
except Exception as e:
    with open('errors.log', 'a') as log:
        log.write(str(e) + '\n')
    sys.exit(1)

palabras = 0
lineas = 0 
for linea in contenido.splitlines():
     lineas =+ 1
     palabras += len(linea.split())

print('Numeros de palabras:',palabras)
print("Numeros de lineas:",lineas)