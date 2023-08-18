# num1 = '12'
# print(type(num1))
# int(num1)+1
# print(type(num1))
# num2 = int(num1)+1


# temp = input('ssss: ')
# a1 = int(temp)+1
# a2 = int(temp)-1
# print(a1)
# print(a2)


#способ 1 (обмен двух переменных через третью)
# a = 12
# b = 3
# temp = a
# a = b
# b = temp
# print('a',a)
# print('b',b)

#способ 2 (обмен двух переменных через третью и четвёртую)
# a = 12
# b = 3
# temp1 = a
# temp2 = b
# a = temp2
# b = temp1
# print('a',a)
# print('b',b)

# #способ 3 (множественное присваивание)
# q1, q2, = 12, 34
# print(q1)
# print(q2)


# a = 12
# b = 3
# temp1 = a
# temp2 = b
# a, b = temp2, temp1  #обмен через временный кортеж
# print('a', a)
# print('b', b)
#
# a = 12
# b = 3
# a,b = b,a
# print('a',a)
# print('b',b)

####################
#
# a = 0
# b = 0
# c = 0
# # или
# a = b = c = 0
# print(a+1)
# print(b+2)
# print(c+3)
# print(a)
# print(a,b,c)


#
# a = b = c = 0
# print(id(a))
# print(id(b))
# print(id(c))
# a = a + 1
# print(id(a))





#Срезы строк

# string = "язык программирования python"
# print(string)
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])


# string = "язык программирования python"
# print(string)
# print(string[3:])   # : уша жойдан дальше укиди
# print(string[2:8])
# print(string[2:8:2])



# string1 = 'программированиa'
# print(string1[0:16:1])


# string1 = 'программирования'
# print(string1[15])


# string1 = 'программирования'
# print(string1[-16])
# print(string1[-1])
# print(string1[-15])
# print(string1[11])


#
#
# string1 = 'программирования'
# print(string1[::-1])   #переворачивает зеркально слово
#
# print(string1[:0])


#####################
# Методы строк
#####################

# string1 = 'I Love python'
# print(string1.lower())       #понижает все буквы
# print(string1.upper())       #увеличивает все буквы
# print(string1.capitalize())       #грамматировать все буквы
# print(string1.title())       #все первые буквы увеличить



# string1 = 'I Love Python'
# a = string1.upper()
# print(a)
# print(string1)


# string1 = 'I Love Python'
# result = string1.lower().startswith('i')
# print(result)
# print(type(result))



# string1 = 'I love Python'
# string1 = string1.lower()
# result = string1.startswith('i')
# print(result)


# string1 = 'I love Python'
# result = string1.lower().startswith('i')
# print(result)
# print(type(result))


# string1 = 'I love Python'
# string2 = string1.replace('Python', 'Linux')
# print(string2)
#
# print(string2.endswith('linux'))



# aaa = chr(ord('a') - 32)
# print(aaa)

# string1 = 'I love Python'
# print(string1.count('I'))

# string1 = 'I love Python'
# print(string1.find('love'))
# print(string1.find('Love'))
# print(type(string1))


# string1 = '     I Lover Python-      '
# string2 = '!!!!!'
# print(string1, string2, sep='')
# string1 = string1.strip()
#
# print(string1, string2, sep='')




# string1 = '     +I love Python - '
# print(string1.strip().rstrip('-').lstrip('+').strip())
#
# string1 = ' + I Love Python - '
# string1 = string1.replace('+','').replace('-','').strip()
# print(string1)



     #split -  разбивает лист
     #strip -  удаляет знак


string1 = 'I:love:Python:bleat'
string2 = string1.split(':')
print(string2)
string3 = ' '.join(string2)
print(string3)




