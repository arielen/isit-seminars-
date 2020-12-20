""" Проверить, является ли заданный одномерный числовой массив упорядоченным по возрастанию """

massive = [-3, 2, 3, 3, 5, 5, 6, 7]
element_min = float('-inf')  # присваем переменной i2 бесконечность в минус степени
found = False

for element in massive:
    if element < element_min:
        if element == element_min:
            break
        found = False
        break
    else:
        found = True
        element_min = element

if found is True:
    print('Все числа идут ПО ВОЗРАСТАНИЮ')
else:
    print('Все числа идут НЕ ПО ВОЗРАСТАНИЮ')
