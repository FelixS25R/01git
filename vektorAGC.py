import vektor

typeOperation = int(input("Indtast 1 for plus, 2 for minus, 3 for skalar: "))

if typeOperation == 1:
    x = int(input("Indtast et tal: "))  
    y = int(input("Indtast et andet tal: "))

    resultatPlus = vektor.regnplus(x, y)
    print(resultatPlus)  # Output: x+y
elif typeOperation == 2:
    x = int(input("Indtast et tal: "))  
    y = int(input("Indtast et andet tal: "))

    resultatMinus = vektor.regnminus(x, y)
    print(resultatMinus)  # Output: x-y
#elif typeOperation == 3:
    #x = int(input("Indtast et tal: "))  
    #y = int(input("Indtast din skalar: "))
    #resultatSkalar = vektor.regnskalar(x, y)
    #print(resultatSkalar)  # Output: x*y