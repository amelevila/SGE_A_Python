num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print (f"Parells:", end=" ")
for i in num:
    if (i%2==0):
        print(f"{i}", end=" ")
print()

print (f"Imparells:", end=" ")
for i in num:
    if (i%2!=0):
        print(f"{i}", end=" ")
print()