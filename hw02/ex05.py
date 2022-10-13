# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

num = int(input("Введите число: "))
num_list = []
for i in range(0, num + 1):
    num_list.append(i)
print(num_list)

k = len(num_list) - 1
for i in num_list:
    temp = num_list[i]
    num_list[i] = num_list[k]
    num_list[k] = temp
    k -= 1
print(num_list)