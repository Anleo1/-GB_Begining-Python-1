from decimal import Decimal
num = Decimal(input("Enter number: "))
sum = 0
if num < 0:
    num *= -1
while num % 1 > 0:
    num = num*10
while num > 0:
    sum += int(num % 10)
    num /= 10
print("Sum elements =", sum)