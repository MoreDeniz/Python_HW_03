# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def nega_fib(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    else:
        return nega_fib(n + 2) - nega_fib(n + 1)

def result_list(n):
    fib_list = []
    for e in range(1, k+1):
        fib_list.append(fib(e))
    null_list = [0]
    nega_list = []
    for e in range(-k, 0):
        nega_list.append(nega_fib(e))
    res = nega_list + null_list + fib_list
    return res

k = int(input('Введите целое число: '))

res = result_list(k)
print(f'для k = {k} список будет выглядеть так: ')
print(res)
