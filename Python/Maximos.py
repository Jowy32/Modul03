numero1 = int(input("Escriba un numero:"))
numero2 = int(input("Escriba otro numero:"))
if (numero1 >= numero2):
    print (numero1)
else:
    print (numero2)
##
##
##
numero1 = int(input("Escriba un numero:"))
numero2 = int(input("Escriba otro numero:"))
numero3 = int(input("Escriba otro numero:"))
if (numero1 >= numero2 >= numero3):
    print (numero1)
else:
    if (numero2 >= numero1 >= numero3):
        print (numero2)
    else:
        print (numero3)
