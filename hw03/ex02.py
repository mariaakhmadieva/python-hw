# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def find_mult(count):
    
    if count < 0:
        print("Negative value of the number of numbers!")
    num_list = sample(range(1, count * 2), count)
    print(num_list)

    mult = []
    i = 0
    new_len = len(num_list) // 2

    if len(num_list) % 2 == 0:
        while i < new_len:
            mult.append(num_list[i] * (num_list[-i-1]))
            i += 1
    else:
        while i < new_len:
            mult.append(num_list[i] * (num_list[-i-1]))
            i += 1
        else:
            mult.append(num_list[i])

    return mult

print(find_mult(int(input("Number of numbers: "))))
