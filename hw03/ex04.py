# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random

def find_difference(count):
    
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = []
    i = 1
    while i <= count:
        list_nums.append(round(random.uniform(0, 10), 2))
        i += 1
    print(list_nums)

    new_list = []
    k = 0
    for k in list_nums:
        new_list.append(round(k % 1, 2))

    diff = print(f'Max:, {max(new_list)}, Min:, {min(new_list)}, Difference: {round(max(new_list) - min(new_list), 2)}')
    return diff

find_difference(int(input("Number of numbers: ")))