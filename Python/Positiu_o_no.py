#  JOC DE PROVES
# 5           Positiu
# 1           Positiu
# -2          No positiu
# 0           Positiu
# -23         No positiu
nombre = int(input("Escriu un nombre qualsevol:"))
if (nombre >= 0):
    print (nombre,"es un nombre positiu")
else:
    print (nombre,"no es un nombre positiu")
    ###############################################################################################################################
    nombre1 = int(input("Escriu un nombre qualsevol:"))
nombre2 = int(input("Escriu un altre nombre:"))
if (nombre1 > nombre2):
    print (nombre2,nombre1)
if (nombre2 > nombre1):
    print (nombre1,nombre2)
else:
    print ("Son el mateix nombre")
    ###############################################################################################################################
    nombre1 = int(input("Escriu un nombre qualsevol:"))
nombre2 = int(input("Escriu un altre nombre:"))
nombre3 = int(input("Escriu un altre nombre:"))
if (nombre1 > nombre2 > nombre3):
    print (nombre3,nombre2,nombre1)
if (nombre1 > nombre3 > nombre2):
    print (nombre2,nombre3,nombre1)
if (nombre2 > nombre3 > nombre1):
    print (nombre1,nombre3,nombre2)
if (nombre2 > nombre1 > nombre3):
    print (nombre3,nombre1,nombre2)
if (nombre3 > nombre2 > nombre1):
    print (nombre1,nombre2,nombre3)
if (nombre3 > nombre1 > nombre2):
    print (nombre2,nombre1,nombre3)
else:
    print ("Hi han dos o mes nombres repetits")
