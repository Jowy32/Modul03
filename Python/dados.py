from random import randint
input ("Pulse una tecla para lanzar el primer dado")
dado_1 = randint (1,6)
print ("El primer dado es:")
if (dado_1 == 1):
    print ("---")
    print ("-o-")
    print ("---")
elif (dado_1 == 2):
    print ("o--")
    print ("---")
    print ("--o")
elif (dado_1 == 3):
    print ("o--")
    print ("-o-")
    print ("--o")
elif (dado_1 == 4):
    print ("o-o")
    print ("---")
    print ("o-o")
elif (dado_1 == 5):
    print ("o-o")
    print ("-o-")
    print ("o-o")
else:
    print ("o-o")
    print ("o-o")
    print ("o-o")
input ("Pulse una tecla para lanzar el segundo dado")
dado_2 = randint (1,6)
print ("El segundo dado es:")
if (dado_2 == 1):
    print ("---")
    print ("-o-")
    print ("---")
elif (dado_2 == 2):
    print ("o--")
    print ("---")
    print ("--o")
elif (dado_2 == 3):
    print ("o--")
    print ("-o-")
    print ("--o")
elif (dado_2 == 4):
    print ("o-o")
    print ("---")
    print ("o-o")
elif (dado_2 == 5):
    print ("o-o")
    print ("-o-")
    print ("o-o")
else:
    print ("o-o")
    print ("o-o")
    print ("o-o")
if (dado_1 + dado_2 == 7) or (dado_1 + dado_2 == 11):
    print ("Usted ha ganado, enhorabuena")
elif (dado_1 + dado_2 == 2) or (dado_1 + dado_2 == 3) or (dado_1 + dado_2 == 12):
    print ("Usted pierde, lo siento")
else:
    print ("Ni gana ni pierde")
