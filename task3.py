# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_list = [1.1, 1.2, 3.1, 5, 10.01]
remains_list=[]

for i in range(len(float_list)):
    remains_list.append(round((float_list[i] - int(float_list[i])), 2))
    
min_elem = remains_list[0]
max_elem = 0
for i in range(len(remains_list)):
    if  max_elem<remains_list[i]:
        max_elem = remains_list[i]

for i in range(len(remains_list)):
    if  min_elem > remains_list[i] > 0:
        min_elem = remains_list[i]

print(f'{float_list} -> {max_elem - min_elem}')





