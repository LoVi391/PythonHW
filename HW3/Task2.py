# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

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
