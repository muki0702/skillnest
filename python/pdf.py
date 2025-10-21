'''nombre = (input("ingresa tu nombre"))
anio = int(input("Ingresa tu año de nacimiento"))
edad = int(input("Ingresa tu edad"))

print(f"Hola {nombre}, naciste en {anio} y tienes {edad} años")

cinco = int(input("Ingresa un Numero"))
if cinco % 2 == 0 and cinco % 5 == 0:
    print("es par y multiplo de 5")
elif cinco % 2 != 0 and cinco % 5 == 0:
    print("es impar y multiplo de 5")
elif cinco % 2 == 0 and cinco % 5 != 0:
    print("es par")
else:
    print("es impar")
cuadrado = int(input("Ingresa un Numero"))
for i in range(1, cuadrado):
    print(f"{i * i}")  
'''

promedio = 0
divisor = 0
while True:
    notas = int(input("Ingresa tus notas"))
    if notas == 0:
        print(f"{promedio/divisor}")
        break
    if notas > 0:
        promedio = promedio + notas
        divisor += 1