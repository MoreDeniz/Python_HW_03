# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def get_list(n):
#     list_num = []
#     for i in range (1, n + 1):
#         list_num.append(random.randint(11, 9999) / 100)
#     return list_num

# def fract_part(list_num):
#     new_list = []
#     for i in range(len(list_num)):
#         num = round(list_num[i] - int(list_num[i]), 2) # зануляем целую часть
#         if num != 0:
#             new_list.append(num)
#     return new_list

# def diff(list_):
#     res = round(max(list_) - min(list_), 2)
#     return res

# import random
# n = int(input('Enter natural number: '))
# list_num = get_list(n)
# print(list_num) 

# fract_list = fract_part(list_num)
# print(fract_list)
# min_fract = round(min(fract_list), 2)
# max_fract = round(max(fract_list), 2)
# print(f'{max_fract } - {min_fract} = {diff(fract_list)}')


from random import randint as RI
n = int(input('Enter natural number: '))
my_list = [RI(11, 9999) / 100 for _ in range(1, n + 1)]

fract_parts = list(map(lambda x: round(x - int(x), 2), my_list))
different = round(max(fract_parts, key = lambda i: round(float(i), 2)) \
            - min(fract_parts, key = lambda i: round(float(i), 2)), 2) 
print(f'{my_list} -> {different}')
