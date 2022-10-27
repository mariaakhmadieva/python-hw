# Вычислить число Пи c заданной точностью d

from decimal import Decimal, getcontext
import math

def is_number(acc):
    try:
        float(acc)
        if float(acc) <= 0 or float(acc) >= 1:
            return print('Incorect number')
        if float(acc) % 2 == 0:
            return print('Incorect number')
        if float(acc) > 0:
            k = 2
            amount = 0
            while k < 100000:
                amount = amount + (1 / k**2)
                k += 1
            pi = math.sqrt((1 + amount) * 6)
            getcontext().prec = abs(acc.find('.') - len(acc))
            print("Pi in required accuracy = ", Decimal(str(pi)) + Decimal(acc) - Decimal(acc))
            return acc
    except ValueError:
        return print('Incorect data')

is_number(input("Enter the required accuracy '0.0001': "))