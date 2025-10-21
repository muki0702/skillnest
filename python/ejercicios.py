
numeros = 0
for i in range(1,50001):
    numeros += i
print(numeros)

pares = 0
for i in range (0, 1001):
    if i % 2 == 0:
        pares += i
print(pares)
impares = 0
for i in range (0,501):
    if i % 2 != 0:
        impares += i
print(impares)

edades = int(input("ingrese una edad"))
if edades > 18: 
    if edades % 2 == 0: 
        print("mayor de edad", "par")
    else: 
        print("mayor de edad", "impar")
else:
    if edades % 2 == 0: print("menor de edad", "par")
    else: print("menor de edad", "impar")

tabla = int(input("ingrese un numero"))
for i in range(1,11):
    print(f"{tabla} x {i} = {tabla * i}")

import random

aleatorio = random.randint(1, 100)