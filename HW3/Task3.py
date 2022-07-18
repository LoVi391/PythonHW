# 3 - Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random


def DiffMaxMin(list):
    diff = 0
    listBuf = []
    for i in range(list.__len__()):
        if(type(list[i]) == float):
            listBuf.append(list[i] % 1)
    diff = round(max(listBuf), 2) - round(min(listBuf), 2)
    return diff
n = int(input('Введите длину списка: '))
listUser = [random.uniform(1, 10)
            for i in range(0, n)]
print(f'Начальный список: {listUser}')
dif = DiffMaxMin(listUser)
print(f"Разница между максимальным и минимальным значением дробной части элементов равна: {dif}")