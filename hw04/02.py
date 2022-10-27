# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def factor(num):

    try:
        int(num)
        num = int(num)
        if num <= 1:
            return print('Incorect number')

        num_list = []
        i = 2
        while i <= num:
            if num % i == 0:
                num_list.append(i)
                num //= i
                i = 2
            else:
                i += 1
        return print('Prime numbers for integer are', num_list)

    except ValueError:
        return print('Incorect data')

factor(input("Enter an integer more than 1 = "))