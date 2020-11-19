"""Найти среднее значение элементов заданного массива размером n,
преобразовать исходный массив, вычитая из каждого элемента среднее значение."""

number = int(input('Введите размер массива >>>  '))
massive = [1, 2, 3, 4, 5, 6, 7, 8]
massive2 = []  # создаем новый массив для дальнейшей замены
element_sum = sum(massive[0:number])  # находим сумму всех элементов по заданный размер
element_avrg = element_sum / len(massive[0:number])  # находим среднее значение элементов по заданный размер

print('Среднее значение элементов:', element_avrg)

for element in massive[0:number]:
    element_new = element - element_avrg
    massive2.append(element_new)
    print('Предыдущий элемент:', element, 'Новое значение элемента:', element_new)

print('Преобразованный массив: ', massive2)
