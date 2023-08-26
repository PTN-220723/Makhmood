#1) Составить таблицу умножения, как на картинке ниже:

# for Bich in range(1, 10):
#     for Rich in range(1, 10):
#        print(f"{Rich*Bich}", end='\t')
#     print()



# 2) Составить программу, которая спрашивает возраст человека и,
# если ему 18 лет и больше, сообщает “Замечательно. Вы уже можете водить автомобиль”,
# а в противном случае – “К сожалению, водить автомобиль Вам рановато”.
# (так же можете сами придумать и добавить вывод сообщения в зависимости от возраста)

# while True:
#     y = int(input('Введите возраст: '))
#     while y >= 18:
#         print('Good,you can drive a car')
#         a = input("let' continue? ")
#         if a.lower() == 'yes':
#             break
#         elif a == 'no':
#
#             print("Exit")
#             break
#     else:
#         print('sorry you cant drive car ')
#         a = input("let' continue? ")
#         if a.lower() == 'no':
#             print('Exit')
#             break

# 3) Создайте игру «Угадай число»,программа генирирует рандомное число в
# заданном интервале, и предлагает пользователю угадать,
# игра продолжается до тех пор пока пользователь угадает число,
# пример игры на картинке ниже:


# print('Привет, Как тебя зовут?')
# name = str(input(''))



#4) Запрограммируйте табло так, чтобы оно по порядку печатало, сколько секунд осталось

# import datetime
# from time import sleep
#
# data = int(input("Укажите время  (в минутах): "))
# time = str(datetime.timedelta(minutes=data))
# h, m, s = time.split(":")
# h, m, s = int(h), int(m) - 1, int(s)
#
# for hour in range(h, -1, -1):
#     for minute in range(m, -1, -1):
#         for second in range(59, -1, -1):
#             print(f'\r{hour}:{minute}:{second}', end='', flush=True)
#             sleep(1)
#     else:
#         m = 59


#5) Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# ёСчастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая выводит на экран все
# доступные счастливые билеты с подсчетом их количество

# cnt = 0
# for a in range(10):
#  for b in range(10):
#   for c in range(10):
#    for d in range(10):
#     for e in range(10):
#      for f in range(10):
#       if a+b+c == d+e+f:
#        cnt +=1
#        print (f" билет №{cnt}:",a,b,c,d,e,f)
#
# print(f"Количество билетов: {cnt}")
# print(f"Всего {round(cnt*100/999999, 2)} %")

#6) Нарисуйте ёлку (вид ёлки произвольный, на картинке только пример) , высоту ёлки должен задавать пользователь

# while True:
#     size = input("Высота елки: ")
#     if size.isdigit():
#         size = int(size)
#         break
#     else:
#         continue
# for i in range(size):
#     print(" " * (size - i - 1), end="")
#     rn = 2 * i + 1
#     for j in range(rn):
#         if i == 0:
#             print("*", end="")
#         elif j == 0:
#             print("/", end="")
#         elif j == rn - 1:
#             print("\\", end="")
#         else:
#             print("*", end="")
#     print()
# if size > 5:
#     print(" " * int(j/2 - 1), end="")
#     print("| |")
# else:
#     print(" " * int(j/2), end="")
#     print("|")