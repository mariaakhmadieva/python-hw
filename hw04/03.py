# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

def rand_num_list(num):

    num = int(num)
    if num <= 0:
        print('Incorect number')
        return []

    list_nums = []
    for i in range(num):
        list_nums.append(randrange(num))

    return list_nums


def unique(list_num):
    result = []
    my_new_dict = {}.fromkeys(list_num, 0)

    for i in list_num:
        my_new_dict[i] += 1

    for k in my_new_dict:
        if my_new_dict[k] == 1:
            result.append(k)

    return result

def unique2(list_num):
    result = []
    for i in list_num:
        if i not in result:
            result.append(i)
    return result

all_list = rand_num_list(int(input("Enter an integer = ")))
print(all_list)
print(unique(all_list))
print(unique2(all_list))