""" Дана матрица А(3, 4). Вычислить и запомнить произведение строк """

matrow0 = [1, 3, 4, 5]
matrow1 = [1, 9, 2, 6]
matrow2 = [5, 2, 4, 7]
matrow0_new = []
matrow1_new = []
matrow2_new = []


def multiply(matrow):
    answer = 1
    for element in matrow:
        answer *= element
    return answer


matrow0_new.append(multiply(matrow0))
matrow1_new.append(multiply(matrow1))
matrow2_new.append(multiply(matrow2))

print('Сумма матрицы:', matrow0, '=', matrow0_new)
print('Сумма матрицы:', matrow1, '=', matrow1_new)
print('Сумма матрицы:', matrow2, '=', matrow2_new)
