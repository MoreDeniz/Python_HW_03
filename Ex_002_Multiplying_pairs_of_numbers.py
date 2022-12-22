# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def get_list():
    my_list = []
    size = int(input('Enter number: '))
    for i in range(size):
        my_list.append(random.randint(0, 9))
    return my_list

def multyplying(my_list):
    multy_list = []
    if len(my_list) % 2 == 0:
        for i in range(0, int(len(my_list)/2), 1):
            multy_list.append(my_list[i] * my_list[len(my_list) - 1 -i])            
    else:
        for i in range(0, int(len(my_list) / 2 + 1), 1):
            multy_list.append(my_list[i] * my_list[len(my_list) - 1 -i]) 
    return multy_list

import random

my_list = get_list()
multy_list = multyplying(my_list)
print(f'{my_list} => {multy_list}')

