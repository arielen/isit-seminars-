""" Вычислить значение функции """

import math

e = 2.718
x = float(input('Введите ваше число  >>> '))

if x < -1:
    a = 1 / 4 * x
elif -1 <= x <= 1:
    a = math.acos(x)
else:
    a = e ** x / 4
print('Ваше значение функции:', a)
