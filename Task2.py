num = int(input("Enter number: "))
sum = 0
if ((num <-999 or num > - 100) and (num < 100 or num > 999)):
    print("Wrong amount of elements in number")
    exit(0)
if num < 0:
    num *= -1
while num > 0:
    sum += int(num % 10)
    num /= 10
print("Sum elements =", sum)