# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции 
# с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def get_list():
#     my_list = []
#     size = int(input('Введите количество элементов списка: '))
#     for i in range(size):
#         my_list.append(random.randint(0, 9))
#     return my_list

# def sum_elems_odd_indexes(my_list):
#     sum = 0
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             sum += my_list[i]
#     return sum

# def odd_index_elems(my_list):
#     odd_elems = []
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             odd_elems.append(my_list[i])
#     return odd_elems

# import random

# my_list = get_list()
# sum = sum_elems_odd_indexes(my_list)
# odd_elems = odd_index_elems(my_list)

# print(my_list, end = '')
# print(f' -> на нечётных позициях элементы: {odd_elems}, ответ: {sum}')

from functools import reduce
from random import randint as RI

my_list = [RI(0, 20) for _ in range(10)]
print(f'В списке: {my_list}')

my_list = [my_list[i] for i in range(10) if i % 2 != 0]
print(f'на нечётных позициях элементы: {my_list}')

summa = reduce((lambda x, y: x + y), my_list)
print(f'Их сумма: {summa}')