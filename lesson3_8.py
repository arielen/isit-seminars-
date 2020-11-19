""" Задан массив D(10). Найти максимальный и минимальный элементы массива D и поменять их местами """
# TODO - не трогать! ПОКА НЕ РАБОТАТЕТ!


massive = [-1, 2, 3, 9, 4, 5, 7, 2, 0, 7]
massive2 = []
max_element = float('-inf')
min_element = float('+inf')

for element in massive:
    if element > max_element:
        max_element = element
        massive2.append(element)
    if element < min_element:
        min_element = element
        massive2.append(element)

max_element = min_element
min_element = max_element

for i in enumerate(massive):
    print(i)

print(massive2)
