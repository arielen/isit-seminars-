a = float(input('Введите число a >>> '))
b = float(input('Введите число b >>> '))
c = float(input('Введите число c >>> '))

#  проверка наименьшего числа
if a < b:
    minim = a
else:
    minim = b
if c < minim:
    minim = c

#  присваивание минимального числа максимальному
if a > b and a > c:
    a = minim
elif b > c and b > a:
    b = minim
else:
    c = minim

print(a, b, c)
