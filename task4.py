# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input())
b = '' 
while num > 0:
    b = str(num % 2) + b
    num = num // 2
 
print(b)
