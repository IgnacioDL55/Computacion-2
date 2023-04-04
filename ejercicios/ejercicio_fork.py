import os
import argparse
import cmath

parser = argparse.ArgumentParser(description="argumento para calcular raices")

parser.add_argument("-n","--number",type=int,help="numero entero")
parser.add_argument("-f","--fork",action="store_true",help="realiza un fork para calcular la raiz negativa")
args = parser.parse_args()

raiz = cmath.sqrt(args.number)

if args.fork:
    ret = os.fork()
    if ret == 0:
        print("Soy el hijo (PID: %d .. PPID: %d )" % (os.getpid(),os.getpid()))
        print(f"Raiz cuadrada negativa: {-raiz}")
    else:
        print("Soy el padre (PID: %d .. PPID: %d )" % (os.getpid(),os.getpid()))
        print(f"Raiz cuadrada positiva: {raiz}")
else:
    print(f"Raiz cuadrada negativa: {-raiz}")


