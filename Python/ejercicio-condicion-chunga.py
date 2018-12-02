num = int(input("Inserte un numero:"))
if (num % 2 == 0) or ((num >= -10) and (num <= 40)) or (num < 0):
    print (num, "entra dentro de los parametros establecidos")
else:
    print (num, "no entra dentro de los parametros establecidos")
