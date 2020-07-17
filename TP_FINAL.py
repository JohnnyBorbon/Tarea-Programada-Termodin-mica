import random
import numpy as np
import matplotlib.pyplot as plt


matriz = []

#Crea listas vacias para almacenar valores de tiempo y entropia que luego
#se usaran para graficar
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




#Creamos una lista vacia para almacenar donde se mueven los 1#
movimiento = []

#Esta función compara la posición donde se encontró el uno con la lista de movimientos
#donde se han movido los unos anteriormente para que un uno no se mueva más de una vez
#por iteración
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


#Esta función recorre la matriz y#
#genera un número aleatorio que dependiendo del número lo mueve una posición
#de manera que si es 1: arriba, 2:abajo, 3:izquierda, 4: derecha
#Este numero se guarda mediante la variable "dirección"
# Y llama a la función mover"
def randomizar():
    global movimiento
    global matriz
    for i in range(0,len(matriz)): 
        for j in range(0,len(matriz[i])):
            mover(i,j)
    movimiento = []

#Esta función comprueba si en la posición encontrada por randomizar se encuentra un 1
#Y comprueba que ese 1 no se haya movido antes mediante la función comprobar
#Si ambas condiciones se cumplen (hay un uno y se va a mover por primera vez)
#utiliza el parametro dirección y comprueba que en esa posición
#hay un 0 (esto para evitar que un 1 caiga en otro 1 por ende se pierdan) 
#y si esto se cumple cambia donde estaba el 1 por un 0, coloca un 1 en la nueva posición
#Y guarda la nueva posición en la lista movimiento

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

#Esta función recorre la matriz en grillas de 10x10 y calcula la cantidad de unos
#en cada grilla 10x10 y calcula la probabilidad como cantidad de unos/100
#estas probabilidades para cada grilla las mete como elementos a una lista
#Algo importante de esta función es que si en una grilla 10x10 la probabilidad es 0
#no introduce esta probabilidad a la lista debido a que el logaritmo natural de 0
#no está definido y asi se elimina este error


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
    
          
#Esta función recorre la lista de las probabilidades para cada grilla 10x10
#Y con cada valor de probabilidad realiza la operación de -p*ln(p) y las suma
#A una variable que almacena estos valores hasta que recorre toda la lista   
#y devuelve la variable entrop que corresponde a la entropia del sistema para este estado   

def calcentrop(listaprob):
    global entrop
    entrop=0
    for i in range(len(listaprob)):
        entrop=entrop+(-1*(listaprob[i])*np.log(listaprob[i]))
    return entrop
        


#La siguiente función realiza la gráfica de la matriz


def graficamostrar(matriz,tiempo):
    plt.figure()
    plt.title("Grilla en el instante t="+str(tiempo+1))
    plt.imshow(matriz,cmap='CMRmap_r')
    plt.show() 

#La siguiente función realiza la gráfica de entropía en función del tiempo, usando una
#Lista para valores de tiempo y otra para valores de entropia    

def graficaentropia(tiempo,entropia):
    plt.figure(6)
    plt.title("Evolución de la entropía en el sistema")
    plt.plot(tiempo,entropia)
    plt.ylabel("Entropía")
    plt.xlabel("Tiempo(pasos)")
    plt.show()

#la función principal del programa, que crea la matriz, realiza las iteraciones y para
#cada iteración calcula la probabilidad en cada grilla 10x10 de la matriz y con esto
#calcula la entropia para dicha iteración iteración(estado)
#Luego inserta el valor del contador de iteraciones en una lista y el valor de la entropia
#en otra lista que luego se usaran para gráficar la entropia contra iteraciones

    
    
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





#Correr el programa principal#
main(20000, 100)
graficaentropia(tiempo,entropia)  
    


