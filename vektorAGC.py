import vektor

x = int(input("Indtast et tal: "))  
y = int(input("Indtast et andet tal: "))

resultatPlus = vektor.regnplus(x, y)
print(resultatPlus)  # Output: x+y


resultatMinus = vektor.regnminus(x, y)
print(resultatMinus)  # Output: x-y

#resultatSkalar = vektor.regnskalar(x, y)
#print(resultatSkalar)  # Output: x*y