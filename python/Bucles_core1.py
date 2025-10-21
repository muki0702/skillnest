print("==Básico==")
for i in range(1, 101):
    print(i)
print("==Multiplos de 2")
for i in range(1, 501):
    if i % 2 == 0:
        print(i)
print("==Ice Ice Baby==")
for i in range(1,1001):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else: 
        print(i)
print("==WoW==")
numeros = 0
for i in range(1,500001):
    numeros += i
print(numeros)
print("==Take me back==")
for i in range(2024, 0, -3):
    print(i)
print("==Contador Dinámico")
numInicial = int(input("Ingresa el numero minimo"))
numFinal = int(input("Ingresa el numero máximo"))
multiplo = int(input("Ingresa el multiplicador común"))
for i in range(numInicial, numFinal+1):
    if i % multiplo == 0:
        print(i)