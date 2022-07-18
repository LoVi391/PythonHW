
#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input('Введите длину списка: '))


def Rnd_lst():
    lst = []
    for i in range(n):
        lst.append(random.randint(1, 10))
    print(f'Cписок:{lst}')
    sum = 0
    for i in range(n):
        if i % 2 > 0:
            sum = sum + lst[i]
    print(f'Сумма чисел, стоящих на нечётных позициях = {sum}')

Rnd_lst()

# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите длину списка: '))

num = [random.randint(-10, 10)

       for i in range(0, n)]
print(f'Начальный список: {num}')

def Mult_num():  
    last = len(num) - 1
    result = [num[i] * num[last - i]
              for i in range(0, (last + 1) // 2)]
    print(f'Список произведений {result}')

Mult_num()