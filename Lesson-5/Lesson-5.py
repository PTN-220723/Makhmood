### while

# x = 0
# while x < 11:
#     print(x)
#     x += 1
# else:
#     x = 0
#
#     print(x, 'shet')



## Цикл while c break - Будет бесконечно спрашивать


# while True:
#     name = input("Add your name: ")
#     if not name:
#         break
#     print(name)
# else:
#     print('Yes')


# cnt = 0
# x = 1
# while x:
#     cnt += 1
#     name = input("Add your name: ")
#     if not name:
#         break
#     elif cnt > 3:
#         x = 0
#     print(name)
# else:
#     print("Yes")


# while True:
#     city = input("Add your city name and enter for Exit:  ").lower()
#     if city:
#         length = len(city)
#     else:
#         print("Exit")
#         break




# Цикл внутри (in) цикла
#
# x = int(input("Введите число: "))
# while x > 0:
#     y = x
#     while y > 0:
#      y -= 1
#      print(y)
#     x -= 1




# FOR цикл
#
# for x in 0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9 , 10:
#     print(x)

# for x in range(11):
#     print(x)

# for x in range(2, 11, 2):
#     if x == 0:
#         continue
#     print(x)
# for x in range(1, 11, 2):
#     print(x)
#

#range (start , stop, step)
# for x in range(0, 11, 2):
#     if x == 0:
#         pass
#     else:
#         print(x)

# for i in range(10, 1, -1):
#       print(i)

# for i in '256':
#     print(i)

# for i in '256':
#     print(i)
# else:
#     print('yes')




#Мин макс

# num_min = input("Add first number: ")
# num_max = input("Add second number: ")
# if num_min.isdigit() and num_max.isdigit():
#     num_min = int(num_min)
#     num_max = int(num_max)
#     if num_min < num_max:
#        for micros in range(num_min, num_max+1):
#          print(f'Квадрат числа {micros} равен {micros**2}')
#     else:
#         for micros in range(num_min, num_max-1, -1 ):
#             print(f'Квадрат числа {micros} равен {micros ** 2}')





#image - рисовать
#
# # rows =int(input("Add number: "))
# cnt = rows = int(input("Add number: "))
# for i in range(1, rows+1):
#     for j in range(cnt):
#         print(i, end=' ')
#     print()
#     cnt -= 1
#
# cnt1 = rows1 = int(input("Add number: "))
# for t in range(1, rows1+1):
#     for k in range(cnt1, 0, -1):
#         print(t, end=' ')
#     print()
#     cnt1 -= 1

#таблица умножения

# for b in range(1, 10):
#     for a in range(1, 10):
#        print(f"{a}x{b}={a*b}", end='\t')
#     print()
#
# for Bich in range(1, 10):
#     for Rich in range(1, 10):
#        print(f"{Rich*Bich}", end='\t')
#     print()


# from time import sleep
#
# # for i in range (10):
# #     print(f'\r{i}', end='')
# #     sleep(1)
#
# while True:
#     for i in '|\\-/':
#      print(f'\r{i}', end='')
#      sleep(1)
