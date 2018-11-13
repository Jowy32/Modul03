figura=input("Que figura quiere calcular (Escriba T o C)?:")
if (figura == "T")or(figura == "t"):
    base=float(input("Indique la base del triangulo:"))
    altura=float(input("Indique la altura del triangulo:"))
    area=(base*altura/2)
    print ("Un triangulo de base",base,"y altura",altura,"tiene un área de",area)
else:
    if (figura == "C")or(figura == "c"):
        radio=float(input("Indique el radio"))
        area=(3.1415*(radio*radio))
        print ("Un circulo de radio",radio,"tiene un área de",area)
    else:
        print ("No calculamos el area de la figura geometrica que desea, disculpe las molestias")
