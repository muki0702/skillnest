while True:
    print("==MENU==")
    print("1)==Básico==")
    print("2)==Multiplos de 2==")
    print("3)==Vanilla Ice==")
    print("4)==WOW==")
    print("5)==Take me back==")
    print("6)==Contador dinámico==")
    print("0)==Salir==")

    menu = int(input("¿Qué quieres hacer hoy?"))
    if menu == 1:
        print("==Básico==")
        for i in range(1, 101):
            print(i)
    elif menu == 2:
        print("==Multiplos de 2")
        for i in range(1, 501):
            if i % 2 == 0:
                print(i)
    elif menu == 3:
        print("==Ice Ice Baby==")
        for i in range(1,1001):
            if i % 10 == 0:
                print("baby")
            elif i % 5 == 0:
                print("ice ice")
            else: 
                print(i)
    elif menu == 4:
        print("==WoW==")
        numeros = 0
        for i in range(1,500001):
            numeros += i
        print(numeros)
    elif menu == 5:
        print("==Take me back==")
        for i in range(2024, 0, -3):
            print(i)
    elif menu == 6:
        print("==Contador Dinámico")
        numInicial = int(input("Ingresa el numero minimo"))
        numFinal = int(input("Ingresa el numero máximo"))
        multiplo = int(input("Ingresa el multiplicador común"))
        for i in range(numInicial, numFinal+1):
            if i % multiplo == 0:
                print(i)
    elif menu == 0:
        break