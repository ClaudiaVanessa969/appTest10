''' Generar un vector de números alearotios de n longitud '''
import os
from random import randint, uniform, random
 
def menu() :
    os.system("cls")
    print("[1] Generar vector de números aleatorios")
    print("[2] Mostrar valores del vector")
    print("[3] Primer valor del vector")
    print("[4] Último valor del vector")
    print("[5] Promedio de los números")
    print("[6] Salir")
    print("")
    print("Escoja una opción: ")
    opcion = int(input())

V = []
i = 0
suma = 0
print("¿Cuántos números aleatorios desea generar?")
n = int(input())

while i < n:
    a = randint(0,100)
    V.append(a)
    suma = suma + a
    i = i + 1

print("*****RESULTADO*****")
print("1) Vector generado: ", V)
print("2) Primer valor del vector: ", V[0])
print("3) Último valor del vector: ", V[n-1])
print("4) Promedio de los números: ", (suma/n))
