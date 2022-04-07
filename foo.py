from sqlite3 import adapt
from urllib.request import UnknownHandler


mapa = []
for i in range(9):
    mapa.append(' ')
def coordenada(literal, inferior, superior):
    while True:
        valor= input(literal)
        while(not valor.isnumeric()):
            print("Solo números entre {0} y {1}".format(inferior,superior)) 
            valor=input(literal)
        coordenada=int(valor)
        if(coordenada>= inferior and coordenada <= superior):
            return coordenada 
        else:
            print("Por favor itroducir un numero entre {0} y {1}".format(inferior,superior))

def ponerFicha(ficha):
    print("da una posición de la ficha")
    while True:
        fila=coordenada("Fila: ", 0,2)
        columna=coordenada("Columna: ", 0,2)
        #como mi tablero es de 3x3
        casilla=fila*3+columna
        if(mapa[casilla]!= ' '):
            print("La casilla está ocupada")
        else:
            mapa[casilla]=ficha
            return
def marcarMapa():
    pos=0
    print(("-"*18))
    for fila in range(3):
        for columna in range(3):
            print("| ",mapa[pos]," ", end='')
            pos+= 1
        print("|\n"),("-"*18)

jugador1 = input("Ingrese nombre jugador 1: ")
jugador2 = input("Ingrese nombre jugador 2: ")

continuar=True
FichasEnElMapa=0
while continuar:
    marcarMapa()
    ponerFicha('x'if (FichasEnElMapa&1)else '0')
    FichasEnElMapa+=1
    if(FichasEnElMapa== 9):
        continuar= False
