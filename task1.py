# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list_numbers = [1, 2, 4, 6, 7, 8]
sum = 0
print(list_numbers)
for i in range(len(list_numbers)):
    if i % 2 != 0:
        sum += list_numbers[i]
print(sum)
