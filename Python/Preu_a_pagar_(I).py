#Colors de cabells:"morens","pelrojos","rossos"
#Sexe:"H","D"
#Python 3.6
Jubilat=input("Estas jubilat/jubilada?:")
Sexe=input("Ets home o dona?:")
Cabells=input("Quin color de cabells tens?:")
if ((Sexe == "D")and(Jubilat == "no")and(Cabells == "rossos"))or(Jubilat == "si"):
    print("No pagues")
if (Sexe=="H")and(Jubilat=="no"):
    print("Pagues 1€")
if ((Sexe=="D")and(Jubilat=="no")and((Cabells=="pelrojos")or(Cabells=="morens"))):
    print("pagues 0,5€")
