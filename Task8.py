n = int(input("Enter one side of chocolate: "))
m = int(input("Enter another side of chocolate: "))
k = int(input("Break off: "))
if (k < n * m ) and ((k % n == 0) or (k % m == 0)):
    print("Possibly")
else:
    print("Impossible")