tabla = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    dni = input("Introduzca el DNI: ")
    letter=dni[-1].upper()
    number=dni[:-1]
    
    if(len(dni)!=9 and number.isdigit()):
        number=int(dni[:-1])
        break
    else:
        print("Format Incorrect")
