num_tic = int(input("Enter number of ticket: "))
sum_first = 0
sum_second = 0
if (num_tic>99999 and num_tic < 1000000):
    first_n = num_tic / 1000
    second_n = num_tic % 1000
    while first_n > 0 and second_n > 0:
        sum_first += int(first_n%10)
        sum_second += int(second_n%10)
        first_n /= 10
        second_n /= 10
    if sum_first == sum_second :
        print("Happy ticket")
    else:
        print("Regular ticket")