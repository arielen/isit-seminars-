"""Задан массив размером 2n.
Сформировать два массива размером n,
включая в первый элемент исходного массива с четными индексами,
а во второй с нечетными"""

massive = [-1, -2, -3, 1, 2, 4, 5]
massive_plus = []
massive_minus = []

for element in massive:
    if element > 0:
        massive_plus.append(element)
    else:
        massive_minus.append(element)

print('Заданный массив: ' + str(massive))
print('Положительные элементы: ' + str(massive_plus))
print('Отрицательные элементы: ' + str(massive_minus))
