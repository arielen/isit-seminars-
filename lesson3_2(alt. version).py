"""Проверить, имеется ли в одномерном числовом массиве хотя бы одна пара соседних чисел, являющихся противоположными"""
# альтернативная версия программы подразумевает полное сравнение чисел,
# однако она также сравнивает первые числа, что делает её неиспользуемой
# TODO - нужно исправить ошибки или полностью переработать.


massive = (1, 2, 2, -3, 4, 5, -1)
found = False

for element in massive:
    for j in massive:
        if element + j == 0:
            found = True  # есть пары
            if element + j != 0:
                found = False  # нет пар
    continue

if found is True:
    print('Есть противоположенные пары чисел')
else:
    print('Нет противоположенных пар чисел')