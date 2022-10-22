# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def find_binary(num):
    if num < 0:
            return "Incorrect number!"

    num_list = []
    while num // 2 != 0:
        if num % 2 == 0:
            num_list.append(0)
        else:
            num_list.append(1)
        num //= 2
    num_list.append(1)
    num_list.reverse()
    bin_num = ''.join(map(str, num_list))
    return bin_num

print(find_binary(int(input("Enter decimal number: "))))
