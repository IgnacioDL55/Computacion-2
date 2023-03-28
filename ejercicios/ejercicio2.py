#!/usr/bin/python3
#Escribir un programa en Python que acepte dos argumentos de línea de comando: 
#una cadena de texto, un número entero. 
#El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero.

import argparse

parse = argparse.ArgumentParser(description='Cadena repetida tantas veces se indique')

parse.add_argument('s','string',type=str,help='cadena de texto')
parse.add_argument('n',type=int,help='cantidad de veces que se repetira la cadena')

args = parse.parse_args()

for i in (args.n):
    print(args.s)
