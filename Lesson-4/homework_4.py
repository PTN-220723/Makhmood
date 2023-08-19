# # 1) Дано целое число. Если оно является положительным то прибавить к нему 20,
# # в противном случае вычесть из него 5. Вывести полученное число
#
num = int(input('Введите число: '))
if num >= 0:
    print(num + 20)
else:
    print(num - 5)

#
#
# #2) Дано два числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2.
#
num1 = int(input('Add first number: '))
num2 = int(input('Add second number: '))
pizdes = num2+num1
if pizdes %5==0:
    print(pizdes+1)
else:
    print(pizdes-2)
#
# #3) Ввести 2 числа. Если их произведение отрицательно, умножить его на 8 и вывести на экран,
# # в противном случае увеличить его в 1,5 раза и вывести на экран.

number = int(input('Add first number: '))
number2 = int(input('Add second number: '))
summ = number+number2
if summ < 0:
    print(summ * 8)
else:
    print(summ * 1.5)

#
#
# #4) Составить программу, которая запрашивает ввод температуры тела человека и определяет, здоров он или болен
#
number33 = int(input('add your temp: '))
if 36 >= number33 >= 36:
    print('Zdorov')
else:
    print('Tebe pizdec')
#
#
#
# #5) Составить программу, которая запрашивает ввод трех значений температуры и проверяет,
# #есть ли среди них температура таяния льда. Если такая температура введена,
# #вывести на экран сообщение «Введена температура таяния льда», иначе «Такой температуры нет»
#
temp1 = int(input('First temp: '))
temp2 = int(input('Second temp: '))
temp3 = int(input('Third temp: '))
if temp2 and temp3 and temp1 >= 0:
    print('«Введена температура таяния льда»')
elif temp2 and temp3 and temp1 <=0:
    print('norm')
else:
    print('«Такой температуры нет»')
#
#
# #6) Составить программу, чтобы компьютер запросил имя пользователя и его год рождения,
# # затем подсчитал возраст человека, в зависимости от года рождения.
#
from datetime import datetime
Year_now = datetime.now().year
Name = input('Enter your name: ')
BirthDate = input('Please enter your year of birth: ')
Birth = int(BirthDate)
print(f'Your age {Year_now - Birth} y.o')
#
#
#
# # 7) Программа спрашивает возраст пользователя.
# # — Если возраст меньше или равен 18, то вывести: «Вам нужно учиться».
# # — Если возраст больше 18, но меньше или равен 50 — «Вам нужно работать»
# # — Если возраст больше 50, но меньше или равен 59 — «Вам скоро на пенсию»
# # — Если возраст больше 59, но меньше 110 — «Вы пенсионер».
# # Также продумайте, что нужно вывести, если пользователь ввел нереальный возраст. Например, 1200.
#
BirthDate = int(input("Введите возраст: "))
if BirthDate <= 18:
    print("Вам нужно учиться")
elif BirthDate > 18 and BirthDate <= 50:
    print("Вам нужно работать")
elif BirthDate > 50 and BirthDate <= 59:
    print("Вам скоро на пенсию")
elif BirthDate > 59 and BirthDate < 110:
    print("Вы пенсионер")
elif BirthDate > 110 and BirthDate <= 200:
    print("Старик как ты до сих пор ходишь живой?")
else:
    print("Вы ввели не верный возраст")


# 8)Напишите программу, которая принимает целое число от 1 до 12 и возвращает название месяца и количество дней.

Month = int(input("Введите число: "))
from datetime import datetime
datetime.now()

if Month == 2:
    print(Month,'28')         # февраль
elif Month <= 7:            # если месяц до июля
    print(Month,30 + Month % 2)    # то к 30 дням добавляем остаток от деления месяца
else:
    print(Month,31 - Month % 2)

print(Month)








