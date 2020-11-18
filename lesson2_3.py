fib0 = 1
fib1 = 1

#  fn=f(n-1)+f(n-2)

#n = input('Введите ваше число Фибоначи >>> ')
n = 40

i = 0
while i < n - 2:
    fib_n = fib0 + fib1
    fib0 = fib1
    fib1 = fib_n
    i += 1

print('Ваше число: ', fib1)
