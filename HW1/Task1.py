# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input(" Введите цифру дня недели, чтобы узнать является ли этот день выходным: "))
# def dayWeek(num):
#   monday = 1
#   tuesday = 2
#   wednesday = 3
#   thusday = 4
#   friday = 5
#   saturday = 6
#   sunday = 7
#   if num == monday:
#     print("Нет")
#   elif num ==tuesday:
#     print("нет")
#   elif num == wednesday:
#     print("нет")
#   elif num == thusday:
#     print("нет")
#   elif num == friday:
#     print("нет")
#   elif num == saturday:
#     print("Да")
#   else:
#     num == sunday
#     print("Да")
    
# dayWeek(num)

def dayWeek(num): 
    if  num in range(1,5): 
        print('Нет') 
    elif num in range(6,7): 
        print('Да') 
    else: 
        print('Такого дня недели нет, напишите цифру от 1 до 7!') 
 
dayWeek(num)