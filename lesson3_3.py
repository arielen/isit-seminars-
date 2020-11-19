""" Проверить, имеется ли в данном одномерном массиве хотя бы одна пара чисел, совпадающих по величине """
# TODO - ДАННЫЙ КОД БЕГАЕТ И БЕРЕТ СТАРЫЕ ЗНАЧЕНИЯ, нужен фикс

massive = [1, 3, 2, 4, 5, 6]
found = False

for element in massive:
    for element2 in massive:
        if element == element2 or element == element2 * (-1):
            found = True  # есть одинаковые числа
            if element != element2:
                found = False  # нет одинаковых чисел

if found is True:
    print('В данном одномерном массиве ЕСТЬ числа совпадающие по величене')
else:
    print('В данном одномерном массиве НЕТ чисел совпадающих по величене')
