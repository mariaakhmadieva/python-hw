#  Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample

def find_sum(count, sum):
    if count < 0:
        return "Negative value of the number of numbers!"
    num_list = sample(range(1, count * 2), count)
    print(num_list)

    sum = sum(num_list[::2])
    return f"Sum of digits is {sum}"

print(find_sum(int(input("Number of numbers: ")), sum))
