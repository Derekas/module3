from typing import Match


numeros=[]
print("1-Add a number to the list")
print("2-Add a number in a position in the list")
print("3-Show the lenght of the list")
print("4-Delete the last number in the list")
print("5-Delete a number in the list")
print("6-Count numbers")
print("7-Position of a numbers")
print("8-Show the list")
print("9-Exit")
opcion=0
while opcion!=9:

    opcion=int(input("Introduzca un numero: "))

    
    if opcion==1:
        numero1=int(input("Introduzca un numero en la lista "))

        numeros.append(numero1)
    elif opcion==2:
        numero2=int(input("Introduzca un numero en la lista "))
        posicion=int(input("Introduzca la posición donde desee poner el numero en la lista "))

        numeros.insert(posicion,numero2)
        
    elif opcion==3:
        print(len(numeros))
    elif opcion==4:
        numeros.pop()
    elif opcion==5:
        posicion=int(input("Introduzca la posición del nunmero que desee eliminar "))
        for i in range(len(numeros)):
            if posicion<=len(numeros):
                if posicion==len(numeros):
                    numeros.pop(posicion)
            else:
                break
    elif opcion==6:
        numero6=int(input(print("Introduzca el numero en la lista que desee contar ")))
        contador=0
        for i in range(len(numeros)):
            if numeros[i]==numero6:
                contador+=1
        print("El numero de veces que se ha encontrado el numero es: ",contador)
    elif opcion==7:
        numero7=int(input("Introduzca un numero en la lista "))
        contador=0
        for i in range(len(numeros)):
            if numeros[i]==numero7:
                print("La posicion del numero es: ",i)
        
    elif opcion==8:
        print(numeros)
    elif opcion==9:
        print("Saliendo..")
        break