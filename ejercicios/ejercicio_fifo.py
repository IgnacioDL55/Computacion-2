import os
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("m1a",type=int,help="row 1,col 1 de la matriz a")
parse.add_argument("m1b",type=int,help="row 1,col 2 de la matriz a")
parse.add_argument("m1c",type=int,help="row 2,col 1 de la matriz a")
parse.add_argument("m1d",type=int,help="row 2,col 2 de la matriz a")

parse.add_argument("m2e",type=int,help="row 1,col 1 de la matriz b")
parse.add_argument("m2f",type=int,help="row 1,col 2 de la matriz b")
parse.add_argument("m2g",type=int,help="row 2,col 1 de la matriz b")
parse.add_argument("m2h",type=int,help="row 2,col 2 de la matriz b")

args = parse.parse_args()

matrix_a = [[args.m1a,args.m1b],[args.m1c,args.m1d]]
matrix_b = [[args.m2e,args.m2f],[args.m2g,args.m2h]]

fifo1 = "fifo_p"

def son_1():
    fifo = open(fifo1,"a")
    result1a = "00:" + str(matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0])
    fifo.write(result1a + "\n" )
    fifo.close()

def son_2():
    fifo = open(fifo1,"a")
    result2a = "01:" + str(matrix_a[0][0] * matrix_b[1][0] + matrix_a[0][1] * matrix_b[1][1])
    fifo.write(result2a + "\n" )
    fifo.close()

def son_3():
    fifo = open(fifo1,"a")
    result3a = "10:" + str(matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0])
    fifo.write(result3a + "\n" )
    fifo.close()

def son_4():
    fifo = open(fifo1,"a")
    result4a = "11:" + str(matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1])
    fifo.write(result4a + "\n" )
    fifo.close()

def father():
    fifo_in = open(fifo1,"r")

    data01 = str(fifo_in.readline().split())
    data02 = str(fifo_in.readline().split())
    data03 = str(fifo_in.readline().split())
    data04 = str(fifo_in.readline().split())

    dataG = [data01,data02,data03,data04]

    for d in dataG:
        if d[:3] == "00:":
            result1 = d[3:]
        elif d[:3] == "01:":
            result2 = d[3:]
        elif d[:3] == "10:":
            result3 = d[3:]
        elif d[:3] == "11:":
            result4 = d[3:]
    
    matrixR = [[result1,result2],[result3,result4]]

    for m in matrixR:
        print(m)


    for m in matrixR:
        print(m)

if not os.path.exists(fifo1):
    os.mkfifo(fifo1)

pid1 = os.fork()
if pid1 == 0:
    father()

    pid2 = os.fork()
    if pid2 == 0:
        son_2()
    else:
        pid3 = os.fork()
        if pid3 == 0:
            son_3()
        else: 
            pid4 = os.fork()
            if pid4 == 0:
                son_4()
else:
    son_1()




