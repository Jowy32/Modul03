# Inicializaciones
salir = "N"
saldo=500
opcion=""

# Mostrar menu
print("Bienvenido al casino/timo")
print("Su saldo es: ",saldo)
print("Que desea hacer amo?")
print("0  Jugar")
print("1  Salir")
opcion=int(input())
if(opcion == 0):
    salir = "N"
else:
    salir = "S"
while ( salir=="N" ):
    # Hago cosas
    apuesta = int(input("Quanto quiere apostar?:"))

    # Jugar
    
    from random import randint
    lado_1 = randint (1,2)
    lado_2 = input("Elige cara o cruz:")
    if (lado_2 == "cara"):
        lado_2 = 2
        if (lado_2 == lado_1):
            gana = "SI"
            print ("Ha salido cara, has ganado")
        else:
            gana = "NO"
            print ("Ha salido cruz, no has ganado")
    else:
        if (lado_2 == "cruz"):
            lado_2 = 1
            if (lado_2 == lado_1):
                gana = "SI"
                print ("Ha salido cruz, has ganado")
            else:
                gana = "NO"
                print ("Ha salido cara, no has ganado")
    # Actualizar saldo
    if(gana=="SI"):
        saldo=saldo+apuesta
    else:
        saldo=saldo-apuesta
    print("")
    print("Su saldo es: ",saldo)
    print("Que desea hacer amo?")
    print("0  Jugar")
    print("1  Salir")
    opcion=int(input())
    # Activo indicador de salida si toca
    if ( saldo<=0 or opcion==1 ): # Condición de salida
        salir = "S"
