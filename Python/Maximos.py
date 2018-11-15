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
##
##
##
mano_der = "mobil"
mano_iz = "bocata"
mano_extra = ""
mano_extra = mano_iz
mano_iz = mano_der
mano_der = mano_extra
print ("mano derecha",mano_der)
print ("mano izquierda",mano_iz)
