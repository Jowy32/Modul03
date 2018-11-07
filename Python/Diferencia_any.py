Any_actual = int(input("Quin any es?:"))
Any_qualsevol = int(input("Escriu un any qualsevol:"))
if (Any_actual == 0)or(Any_qualsevol == 0):
    print ("L'any 0 no existeix")
else:
    if (Any_actual == Any_qualsevol):
        print ("Son el mateix any!")
    else:
        if (Any_actual < 0)and(Any_qualsevol < 0)and(Any_actual < Any_qualsevol):
            res = (Any_qualsevol)-(Any_actual)
            print ("Per arribar al any",Any_qualsevol,"falten",res, "anys")
        if (Any_actual < 0)and(Any_qualsevol < 0)and(Any_actual > Any_qualsevol):
            res = (Any_actual)-(Any_qualsevol)
            print ("Han passat",res,"anys desde l'any",Any_qualsevol,)
        else:
            if (Any_actual > 0)and(Any_qualsevol > 0)and(Any_actual < Any_qualsevol):
                res = (Any_qualsevol) - (Any_actual)
                print ("Per arribar al any",Any_qualsevol,"falten",res," anys")
            if (Any_actual > 0)and(Any_qualsevol > 0)and(Any_actual > Any_qualsevol):
                res = (Any_actual) - (Any_qualsevol)
                print ("Han passat",res,"anys desde l'any",Any_qualsevol,)
