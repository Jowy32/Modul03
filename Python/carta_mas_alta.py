from random import randint
valor_carta_1 = randint (2,14)
if (valor_carta_1 >= 2) and (valor_carta_1 <= 10):
    carta_1 = valor_carta_1
else:
    if (valor_carta_1 == 11):
        carta_1 = "J"
    else:
        if (valor_carta_1 == 12):
            carta_1 = "Q"
        else:
            if (valor_carta_1 == 13):
                carta_1 = "K"
            else:
                if (valor_carta_1 == 14):
                    carta_1 = "A"
valor_carta_2 = randint (2,14)
if (valor_carta_2 >= 2) and (valor_carta_2 <= 10):
    carta_2 = valor_carta_2
else:
    if (valor_carta_2 == 11):
        carta_2 = "J"
    else:
        if (valor_carta_2 == 12):
            carta_2 = "Q"
        else:
            if (valor_carta_2 == 13):
                carta_2 = "K"
            else:
                if (valor_carta_2 == 14):
                    carta_2 = "A"
print ("La carta 1 es",carta_1)
print ("La carta 2 es",carta_2)
if (valor_carta_2 > valor_carta_1):
    print ("La carta 2 gana")
else:
    if (valor_carta_2 < valor_carta_1):
        print ("La carta 1 gana")
    else:
        print ("Es un empate")
