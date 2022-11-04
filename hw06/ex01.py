# Напишите программу, которая принимает на вход число и исключает кратные 2 и 5 
# и составляет список пар (число; квадрат числа) из оставшихся

num = int(input("Enter an integer = "))
if num > 0:
    data = [x for x in range(num)]
    res = filter(lambda x: x%5, data)
    res = filter(lambda x: x%2, res)
    res = list(map(lambda x: (x, x**2), res))
    print(*res)
else:
    print('Incorect number')