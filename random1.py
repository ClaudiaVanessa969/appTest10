#randint: genera numeros enteros aleatorios
#uniform: genera numeros flotantes aleatorios

import os
from random import randint, uniform, random

def Z():
    a = randint(0,100)
    return a

def R():
    b = uniform(0,100)
    return b

print("The Z number generate is: ", Z())
print("The R number generate is: ", R())

