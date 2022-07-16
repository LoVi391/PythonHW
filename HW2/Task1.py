# 1 - Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


# str_num = input('введите вещественное число:' )
# def Check_num(str_num):
#     if str_num.isdigit():
#         print(str_num)
#     else:
#         return('не число')  #не удалось правлильно выйти из проверки
# print(Check_num(str_num))

#str_num = 0
str_num = str(input('введите вещественное число:' ))
# def check_num():
#     while True:
        
#         if str_num.isdigit():
#             return str_num           #пока не получается с проверкой буду еще думать
        
#         print('incorrect')
# print(check_num(str_num))
sum = 0
for i in str_num:
        if i!=".":
            sum = sum + int(i)
print(f"Сумма цифр числа {str_num} равна: ", sum)
