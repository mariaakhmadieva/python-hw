# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


num = input("Введите число: ")
num  = float(num ) * 10 ** len(num )
sum = 0

while num  > 0:
    digit = num  % 10
    sum = sum + digit
    num  = num  // 10

print(str(sum).replace('.', '').replace('0',''))