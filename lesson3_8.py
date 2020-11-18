""" Задан массив D(10). Найти максимальный и минимальный элементы массива D и поменять их местами """

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


for i in enumerate(massive):
    print(i)

massive2.append(massive)
print(massive2)