num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print (f"Parells:", end=" ")
sumaParells = 0
for i in num:
    if (i%2==0):
        sumaParells += i
        print(f"{i}", end=" ")
print()
print(f"Suma parells: {sumaParells}")

print()

print (f"Imparells:", end=" ")
sumaImparells = 0
for i in num:
    if (i%2!=0):
        sumaImparells += i
        print(f"{i}", end=" ")
print()
print(f"Suma imparells: {sumaImparells}")