from random import randint
lado_1 = randint (1,2)
lado_2 = input("Elige cara o cruz:")
if (lado_2 == "cara"):
    lado_2 = 2
    if (lado_2 == lado_1):
        print ("Ha salido cara, has ganado")
    else:
        print ("Ha salido cruz, no has ganado")
else:
    if (lado_2 == "cruz"):
        lado_2 = 1
        if (lado_2 == lado_1):
            print ("Ha salido cruz, has ganado")
        else:
            print ("Ha salido cara, no has ganado")
