# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

count = input("Enter a degree of a polynomial more than 1 = ")
try:
    int(count)
    count = int(count)
    if count <= 1:
        print('Incorect number')

    if count > 1:
        coeffs = []
        for i in range(count + 1):
            num = randint(0, 100)
            coeffs.append(num)

        result = ''
        for i in range(len(coeffs)-2):
            if coeffs[i] == 0:
                continue
            result = result + str(coeffs[i]) + 'x^' + str(count - i)
            if coeffs[i] > 0:
                result = result + ' + '

        if coeffs[i+1] != 0:
            result = result + str(coeffs[i+1]) + 'x'
        else:
            result = result.rstrip(' + ')
        if coeffs[i+2] != 0:
            result = result + ' + ' + str(coeffs[i+2])
        else:
            result = result.rstrip(' + ')

        result = result + ' = 0'

        print(coeffs)
        print(result)
    
        with open("result.txt", "a", encoding="utf-8") as my_f:
            my_f.write(f'{result}\n')

except ValueError:
    print('Incorect data')