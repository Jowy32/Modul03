dividendo = int(input("Escriba el dividendo:"))
divisor = int(input("Escriba el divisor:"))
if (dividendo == divisor):
    print ("Las soluciones son infinitas!")
if (dividendo != 0) and (divisor == 0):
    print ("No se puede dividir entre 0")
if (dividendo != 0) and (divisor != 0):
    cociente = (dividendo // divisor)
    resto = (dividendo % divisor)
    if (resto == 0):
        print ("La division es exacta. Cociente:",cociente)
    if (resto != 0):
        print ("La division no es exacta. Cociente:",cociente, "Resto:",resto)
if (dividendo == 0) and (divisor != 0):
    print ("La division es exacta. Cociente: 0")
