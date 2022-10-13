# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

num = int(input("Введите число: "))
num_list = []
for i in range(-num, num + 1):
    num_list.append(i)
print(num_list)

p1 = int(input("Введите первую позицию: "))
p2 = int(input("Введите вторую позицию: "))

if 0 < p1 < len(num_list) + 1 and 0 < p2 < len(num_list) + 1:
    print("Произведение чисел равно:", num_list[p1 - 1] * num_list[p2 - 1])
else:
    print("Введена неверная позиция")