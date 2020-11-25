"""" Проверить, имеется ли в одномерном числовом массиве
хотя бы одна пара соседних чисел, являющихся противоположными"""

massive = [1, 1, 2, -2, 3, 2, 4, 5, -4, 6]
element2 = 0  # element2 - является предыдущим числом element
found = False

for element in massive:
    if element == element2 * (-1):
        found = True  # Есть противоположенные пары чисел
        continue
    else:
        element2 = element
        element += 1

if found is True:
    print('ЕСТЬ противоположенные пары чисел, стоящие рядом')
else:
    print('НЕТ противоположенных пар чисел, стоящих рядом')
