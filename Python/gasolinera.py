print ("Que tipo de gasolina quiere?")
print ("Super: Normal(1.5€)(S1), Turbo(1.55€)(S2)")
print ("Sin plomo: Normal(1.6€)(Sp1), Con aditivos(sabor naranja)(1.65€)(Sp2)")
print ("Diesel: Normal(1.7€)(D1), Fast&Furius(1.75€)(D2)")
gasolina = input()
litros = float(input("Quantos litros quiere?:"))
if (gasolina == "S1"):
    precio = (1.5 * litros)
    print ("Serán" ,precio, "€")
else:
    if (gasolina == "S2"):
        precio = (1.55 * litros)
        print ("Serán" ,precio, "€")
    else:
        if (gasolina == "Sp1"):
            precio = (1.6 * litros)
            print ("Serán" ,precio, "€")
        else:
            if (gasolina == "Sp2"):
                precio = (1.65 * litros)
                print ("Serán" ,precio, "€")
            else:
                if (gasolina == "D1"):
                    precio = (1.7 * litros)
                    print ("Serán" ,precio, "€")
                else:
                    if (gasolina == "D2"):
                        precio = (1.75 * litros)
                        print ("Serán" ,precio, "€")
