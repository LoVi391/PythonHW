# 2. Напишите программу, которая принимает на
# вход число N и выдает набор произведений чисел от 1
# до N. Факториал
# 5! = 120

n=int(input('Введите число: '))
factor = 1
for i in range(1, n+1):
    factor=factor * i
print(factor)