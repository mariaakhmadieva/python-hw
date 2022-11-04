# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

num = (int(input("Enter an integer = ")))
if num <= 0:
    print('Incorect number')
list_nums = [randint(1, 10) for i in range(num)]
print(list_nums)

unique1 = [i for i in list_nums if list_nums.count(i) == 1]
print(unique1)