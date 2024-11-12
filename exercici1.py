num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input ("Introdueix el segon nombre: "))
if num1>num2:
    print (f"{num1} és més gran que {num2}")
elif num2>num1:
    print (f"{num2} és més gran que {num1}")
else:
    print ("Els dos nombres són iguals")