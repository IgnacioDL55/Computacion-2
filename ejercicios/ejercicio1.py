#!/usr/bin/python3
#Escribir un programa en Python que acepte un número de argumento entero positivo n 
#y genere una lista de los n primeros números impares. 
#El programa debe imprimir la lista resultante en la salida estandar. 

import argparse

parser = argparse.ArgumentParser(description="Generear lista n con numeros impares")

parser.add_argument('n',type=int,help='lista n con numeros enteros')

args = parser.parse_args()

odd_number = [2*i + 1 for i in range(args.n)]

print(odd_number)