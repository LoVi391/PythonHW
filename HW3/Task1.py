
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
