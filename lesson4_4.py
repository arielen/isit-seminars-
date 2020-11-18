""" Дана целочисленная квадратная матрица В размера nxn.
Найти номер столбцов, все элементы которых - нули """

massive1 = [1, 3, 0, 4, 0, 6, 7, 8, 9]
massive2 = [1, 0, 2, 4, 0, 6, 7, 8, 9]

for element in massive1:
    for element2 in massive2:
        while element + element2 == 0:
            print('nul')

        pass
    break
