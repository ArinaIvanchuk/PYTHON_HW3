# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input('input number k: ')) + 1
def completion_negafib_list(list_fibonacci):
    nega_list = []
    for i in range(len(list_fibonacci)):

        if i % 2 != 0:
            nega_list.append(list_fibonacci[i])
        else:
            nega_list.append(list_fibonacci[i] * (-1))
    return nega_list

list_fibonacci = list(fibonacci(n))

list_negafibonacci=list(completion_negafib_list(list_fibonacci))


list_negafibonacci.reverse()
print (f'sequence generation: {list_negafibonacci[:-1] + list_fibonacci}')