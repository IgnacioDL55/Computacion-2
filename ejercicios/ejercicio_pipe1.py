import os
import argparse

parse = argparse.ArgumentParser(description="Contar palabras del texto")
parse.add_argument("texto",help="argumento del texto")
args = parse.parse_args()

r,w = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(w)
    doc = os.read(r,2024)
    file = doc.decode()
    word = file.split("\n")
    count = 0
    f = 1
    for w in word:
        count = len(w.split())
        print(f"El numero de palabras en la linea {f} es: {count}")
        f += 1
    os.close(r)
else:
    os.close(r)
    try:
        with open(args.texto ,"r") as f:
            for line in f:
                os.write(w, line.encode())
    except BrokenPipeError as e:
        print("Ocurrio un error,el pipe esta roto ", e)
    os.close(w)
