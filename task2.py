# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
def product_list_couples (list):
    num_prod_list = []
    for i in range (1,(math.ceil(len(list)/2)+1)):
        num_prod_list.append(list[i-1]*list[-i])
    return num_prod_list
list_num = [2, 3, 4, 5, 6] 
print(product_list_couples(list_num))