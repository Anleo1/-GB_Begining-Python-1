num = int(input("Enter number: "))
if num % 6 != 0:
    print("Wrong number (not an integer number of shadoofs)")
    exit(0)
amount_P = int(num / 6)
amount_S = amount_P
amount_K = 2*(amount_P + amount_S)
print("Petya and Sergey =", amount_P, "Katya =", amount_K)