import random
import numpy as np
import matplotlib.pyplot as plt


matriz = []


tiempo=[]
entropia=[]


#Crea la matriz cuadrada#
def crearMatriz(size):
    global matriz
    matriz=[]
    fila=0
    while fila!=size:
        lista=[]
        i=0
        while i<size:
            lista.append(0)
            i+=1
            if len(lista)==size:
                matriz.append(lista)
        fila+=1

    centro= [int((size//2)-(size*0.05)),int((size//2)+(size*0.05))]

    for i in range(centro[0],centro[1]): 
        for j in range(centro[0],centro[1]):
            matriz[i][j] = 1





movimiento = []


def comprobar(pos):
    global movimiento
    if movimiento == []:
        return True
    else:
        tmp = True
        for a in movimiento:
            if a == pos:
                tmp = False
        return tmp



def randomizar():
    global movimiento
    global matriz
    for i in range(0,len(matriz)): 
        for j in range(0,len(matriz[i])):
            mover(i,j)
    movimiento = []



def mover(i,j):
    global matriz
    while True:
        direccion = random.randint(1, 4)
        if matriz[i][j] == 1 and comprobar([i, j]):
            if direccion == 1 and ((i-1)>=0):
                if matriz[i - 1][j] == 0:
                    matriz[i][j] = 0
                    matriz[i - 1][j] = 1
                    movimiento.append([i - 1, j])
            elif direccion == 2and ((i+1)<len(matriz)):
                if matriz[i + 1][j] == 0: 
                    matriz[i][j] = 0
                    matriz[i + 1][j] = 1
                    movimiento.append([i + 1, j])
            elif direccion == 3 and ((j-1)>=0):
                if matriz[i][j - 1] == 0:
                    matriz[i][j] = 0
                    matriz[i][j - 1] = 1
                    movimiento.append([i, j - 1])
            elif direccion == 4 and ((j+1)<len(matriz)):
                if matriz[i][j + 1] == 0:
                    matriz[i][j] = 0
                    matriz[i][j + 1] = 1
                    movimiento.append([i, j + 1])   
        break




def calcprob(matriz):
    global listaprob
    listaprob=[]
    prob=0       
    cont1=0
    for f in range (0,10):
        for i in range(10*f,(10+10+f)):
            for g in range(0,10):
                for j in range(10*g,(10+10*g)):
                    if matriz[i][j]==1:
                        cont1+=1
            prob=cont1/100
            if prob!=0:
                listaprob.append(prob)
            
    return listaprob
    
          


def calcentrop(listaprob):
    global entrop
    entrop=0
    for i in range(len(listaprob)):
        entrop=entrop+(-1*(listaprob[i])*np.log(listaprob[i]))
    return entrop
        





def graficamostrar(matriz,tiempo):
    plt.figure()
    plt.title("Grilla en el instante t="+str(tiempo+1))
    plt.imshow(matriz,cmap='CMRmap_r')
    plt.show() 



def graficaentropia(tiempo,entropia):
    plt.figure(6)
    plt.title("Evolución de la entropía en el sistema")
    plt.plot(tiempo,entropia)
    plt.ylabel("Entropía")
    plt.xlabel("Tiempo(pasos)")
    plt.show()


    
    
def main(iteraciones,size):
    global tiempo
    global entropia
    crearMatriz(size)
    i = 0
    graficamostrar(matriz,-1)
    while i < iteraciones:
        randomizar()
        calcprob(matriz)
        calcentrop(listaprob)
        tiempo.append(i)
        entropia.append(entrop)
        if i==9 or i==99 or i==999 or i==9999:
           graficamostrar(matriz,i) 
        i+=1



main(20000, 100)
graficaentropia(tiempo,entropia)  
    


