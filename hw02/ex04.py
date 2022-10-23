# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
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
    with open("file.txt", "a", encoding="utf-8") as my_f:
        res = num_list[p1- 1] * num_list[p2 - 1]
        my_f.write(f'{res}\n')
else:
    print("Введена неверная позиция")
