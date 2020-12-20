""" Дана целочисленная квадратная матрица В размера nxn.
Найти номер столбцов, все элементы которых - нули """
# TODO - не трогать!!!
#  матрица квадратная и равна ( n x n )

massive1 = [1, 3, 0, 4, 1, 6, 7, 8, 0]
massive2 = [1, 0, 2, 4, 0, 6, 7, 8, 0]
count = 0

for element in massive1:
    count += 1
    if element == 0:
        if massive2[count-1] == 0:
            print(massive2[count-1], element)
            print('Столбец:', count)


