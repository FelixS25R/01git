import vektor

typeOperation = int(input("Indtast 1 for plus, 2 for minus, 3 for skalar: "))

if typeOperation == 1:
    x1 = int(input("Indtast et tal: "))  
    y1 = int(input("Indtast et andet tal: "))
    x2 = int(input("Indtast et tal: ")) 
    y2 = int(input("Indtast et tal: "))

    resultatPlus = vektor.regnplus(x1, y1, x2, y2)
    print(resultatPlus)  # Output: x1+y1
elif typeOperation == 2:
    x1 = int(input("Indtast et tal: "))  
    y1 = int(input("Indtast et andet tal: "))
    x2 = int(input("Indtast et tal: ")) 
    y2 = int(input("Indtast et tal: "))

    resultatMinus = vektor.regnminus(x1, y1,x2,y2)
    print(resultatMinus)  # Output: x1-y1
elif typeOperation == 3:
    x1 = int(input("Indtast et tal: "))  
    y2 = int(input("Indtast et tal: "))
    s = int(input("Indtast din skalar: "))
    resultatSkalar = vektor.regnskalar(x1, y2, s)
    print(resultatSkalar)  # Output: x1*y2