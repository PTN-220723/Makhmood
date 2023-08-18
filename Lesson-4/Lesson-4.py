## kto bolshe
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# if num1 > num2:
#     print('Первое числло больше второго')
# elif num1 < num2:
#     print('Второе число больше второго')
# else:
#     print('Числа равны')


#Задача с купе - 1
# num = int(input('Ваш билет: '))
# if num %4 ==0:
#     print(f'Номер в купе: {num//4}')
# else:
#     print(f'Номер в купе: {num // 4+1}')

#Задача с купе - 2
# num = int(input('Your bilet: '))
# print('Номер в купе: ', num // 4 + (num%4 > 0))


# #Weather task
# city = input('Введите название города: ').lower()
# if not city:
#     print("Вы не указали название города")
#     print("Запустите скрипт еще раз")
#     exit()
# lenght = len(city)
# if city == "Tashkent"[0:lenght]:
#     print("В ташкенте тепло и солнечно")
# elif city == "London"[0:lenght]:
#     print(" В Лондоне пасмурно и сыро ")
# elif city == "Moskow"[0:lenght]:
#     print("Идёт сильный дождь")
# elif city == "rio de janeyro"[0:lenght]:
#     print("В Рио постоянно карнавалы")
# else:
#     print(" Прогно не ясен ")




# #Weathertask-2
city = input('Введите название города: ').lower()
lenght = len(city)
if city:
    lenght = len(city)
    if city == "Tashkent"[0:lenght]:
        print("В ташкенте тепло и солнечно")
    elif city == "London"[0:lenght]:
        print(" В Лондоне пасмурно и сыро ")
    elif city == "Moskow"[0:lenght]:
        print("Идёт сильный дождь")
    elif city == "rio de janeyro"[0:lenght]:
        print("В Рио постоянно карнавалы")
    else:
        print(" Прогноз не ясен ")




# #factoty task - 1 variant
#
day = int(input("what day is today: "))
if day >= 1 and day <= 10:
    print("milk")
elif day >= 11 and day <= 20:
    print("Cheese")
elif day >= 21 and day <= 28:
    print("meat")
elif day > 31:
    print("ti debil , kalendar ne imeet 32 dnya")
else:
    print('Holiday')

#factoty task - 2 variant
# day = int(input("what day is today: "))
# if  1 <= day <= 10:
#     print("milk")
# elif  day <= 20:
#     print("Cheese")
# elif  day <= 28:
#     print("meat")
# elif  day > 31:
#     print("ti debil , kalendar ne imeet 32 dnya")
# else:
#     print('Holiday')

# #factoty task - 3 variant
# from datetime import datetime
# current_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S") #
# #day = current_time.day
# day = datetime.now().day
# if  1 <= day <= 10:
#     print("milk")
# elif  day <= 20:
#     print("Cheese")
# elif  day <= 28:
#     print("meat")
# elif  day > 31:
#     print("ti debil , kalendar ne imeet 32 dnya")
# else:
#     print('Holiday')



# ### Morjoviy operator (walrus)
# print( num := 15)
#
# #без маржовый оператор
# text = "I love python "
# if len(text) > 5:
#     print(len(text))
#
# #маржовый оператор   3.8
# text = "I love python "
# if (a := len(text)) > 5:
#     print(a)


#тернарное выражение if/else (самая коротая версия if)

# a = 4
# num = 0 if a//4 == 0 else 1
# print(num)










