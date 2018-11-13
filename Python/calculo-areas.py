figura=input("Que figura quiere calcular (Escriba T o C):?")
if (figura == "T")or(figura == "t"):
    base=int(input("Indique la base del triangulo:"))
    altura=int(input("Indique la altura del triangulo:"))
    area=(base*altura/2)
    print ("Un triangulo de base",base,"y altura",altura,"tiene un área de",area)
if (figura == "C")or(figura == "c"):
    radio=int(input("Indique el radio"))
    area=(3.1415*(radio*radio))
    print ("Un circulo de radio",radio,"tiene un área de",area)
else:
    print ("No calculamos el area de la figura geometrica que desea, disculpe las molestias")
