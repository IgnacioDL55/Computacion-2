import math
import threading as th

def calcular_t(n, x):
    global lista_t
    lista_t.append(((-1)**n/math.factorial(2*n+1))*x**(float(2*n+1)))

def suma():
    global lista_t
    global suma_total
    suma_total = 0
    for i in lista_t:
        suma_total += i

if __name__ =='__main__':
    lista_t = []
    suma_total = 0
    n = int(input('Inserte numero de terminos: '))
    x = float(input('Inserte valor de x: '))
    hilos = []

    for i in range(n):
        hilo = th.Thread(target= calcular_t, args=(i,x))
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

    hilo_suma = th.Thread(target=suma)
    hilo_suma.start()
    hilo_suma.join()

    print(f'Number of terms: {n}')
    print(f'X = {suma_total}')
    print(f'Reference value: {math.sin(x)}')
    print(f'Error: {abs(suma_total-math.sin(x))}')
