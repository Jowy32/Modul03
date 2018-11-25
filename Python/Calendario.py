for num_dia in range(0, 365):
    if ((num_dia + 1) >=1) and ((num_dia +1) <= 31):
        print (num_dia + 1, "de Enero")
    if ((num_dia + 1) >=32) and ((num_dia +1) <= 59):
        print ((num_dia + 1) - 31, "de Febrero")
    if ((num_dia + 1) >=60) and ((num_dia +1) <= 90):
        print ((num_dia + 1) - 59, "de Marzo")
    if ((num_dia + 1) >=91) and ((num_dia +1) <= 120):
        print ((num_dia + 1) - 90, "de Abril")
    if ((num_dia + 1) >=121) and ((num_dia +1) <= 151):
        print ((num_dia + 1) - 120, "de Mayo")
    if ((num_dia + 1) >=152) and ((num_dia +1) <= 181):
        print ((num_dia + 1) - 151, "de Junio")
    if ((num_dia + 1) >=182) and ((num_dia +1) <= 212):
        print ((num_dia + 1) - 181, "de Julio")
    if ((num_dia + 1) >=213) and ((num_dia +1) <= 243):
        print ((num_dia + 1) - 212, "de Agosto")
    if ((num_dia + 1) >=244) and ((num_dia +1) <= 273):
        print ((num_dia + 1) - 243, "de Septiembre")
    if ((num_dia + 1) >=274) and ((num_dia +1) <= 304):
        print ((num_dia + 1) - 273, "de Octubre")
    if ((num_dia + 1) >=305) and ((num_dia +1) <= 334):
        print ((num_dia + 1) - 304, "de Noviembre")
    if ((num_dia + 1) >=335) and ((num_dia +1) <= 365):
        print ((num_dia + 1) - 334, "de Diciembre")
##
##
##
##Mejora 1:
anyo = int(input("Inserte un año:"))
if (anyo % 4 == 0):
    for num_dia in range(0, 366):
        if ((num_dia + 1) >=1) and ((num_dia +1) <= 31):
            print (num_dia + 1, "de Enero")
        if ((num_dia + 1) >=32) and ((num_dia +1) <= 60):
            print ((num_dia + 1) - 31, "de Febrero")
        if ((num_dia + 1) >=60) and ((num_dia +1) <= 91):
            print ((num_dia + 1) - 59, "de Marzo")
        if ((num_dia + 1) >=92) and ((num_dia +1) <= 121):
            print ((num_dia + 1) - 91, "de Abril")
        if ((num_dia + 1) >=122) and ((num_dia +1) <= 152):
            print ((num_dia + 1) - 121, "de Mayo")
        if ((num_dia + 1) >=153) and ((num_dia +1) <= 182):
            print ((num_dia + 1) - 152, "de Junio")
        if ((num_dia + 1) >=183) and ((num_dia +1) <= 213):
            print ((num_dia + 1) - 182, "de Julio")
        if ((num_dia + 1) >=214) and ((num_dia +1) <= 244):
            print ((num_dia + 1) - 213, "de Agosto")
        if ((num_dia + 1) >=245) and ((num_dia +1) <= 274):
            print ((num_dia + 1) - 244, "de Septiembre")
        if ((num_dia + 1) >=275) and ((num_dia +1) <= 305):
            print ((num_dia + 1) - 274, "de Octubre")
        if ((num_dia + 1) >=306) and ((num_dia +1) <= 335):
            print ((num_dia + 1) - 305, "de Noviembre")
        if ((num_dia + 1) >=336) and ((num_dia +1) <= 367):
            print ((num_dia + 1) - 335, "de Diciembre")
else:
    for num_dia in range(0, 365):
        if ((num_dia + 1) >=1) and ((num_dia +1) <= 31):
            print (num_dia + 1, "de Enero")
        if ((num_dia + 1) >=32) and ((num_dia +1) <= 59):
            print ((num_dia + 1) - 31, "de Febrero")
        if ((num_dia + 1) >=60) and ((num_dia +1) <= 90):
            print ((num_dia + 1) - 59, "de Marzo")
        if ((num_dia + 1) >=91) and ((num_dia +1) <= 120):
            print ((num_dia + 1) - 90, "de Abril")
        if ((num_dia + 1) >=121) and ((num_dia +1) <= 151):
            print ((num_dia + 1) - 120, "de Mayo")
        if ((num_dia + 1) >=152) and ((num_dia +1) <= 181):
            print ((num_dia + 1) - 151, "de Junio")
        if ((num_dia + 1) >=182) and ((num_dia +1) <= 212):
            print ((num_dia + 1) - 181, "de Julio")
        if ((num_dia + 1) >=213) and ((num_dia +1) <= 243):
            print ((num_dia + 1) - 212, "de Agosto")
        if ((num_dia + 1) >=244) and ((num_dia +1) <= 273):
            print ((num_dia + 1) - 243, "de Septiembre")
        if ((num_dia + 1) >=274) and ((num_dia +1) <= 304):
            print ((num_dia + 1) - 273, "de Octubre")
        if ((num_dia + 1) >=305) and ((num_dia +1) <= 334):
            print ((num_dia + 1) - 304, "de Noviembre")
        if ((num_dia + 1) >=335) and ((num_dia +1) <= 365):
            print ((num_dia + 1) - 334, "de Diciembre")
