# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_num = int(input("Введите натуральное число: "))
binar_num = ''

print(f'{decimal_num} ->', end = ' ')

while decimal_num > 0:
    binar_num = str(decimal_num % 2) + binar_num
    decimal_num = decimal_num // 2

print(binar_num)