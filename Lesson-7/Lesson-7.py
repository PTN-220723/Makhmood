# #dict (словарь)
#1 способ
# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan'}
# print(city['name'])
# city2 = {0: 'Tashkent', 1:30000, 2:3400000, 3:'Uzbekistan'}
# print(city2[0])
# print(type(city2))
#
#
# #list
# city_list = ['Tashkent', 30000, 34000000, 'Uzbekistan']
# print(city_list[0])


# #tuple
# city_tuple = ('Tashkent', 30000, 3400000,'Uzbekistan')
# print(city_tuple[0])
#-------------------------------------------------------------------#


#2 способ
# city2 = dict(name= 'tashkent', size=30000, people=3000000, country='Uzbekistan')
# print(type(city2))
# print(city2)

#3 способ
# action = ['like', 'dislike']
# all_action = dict.fromkeys(action, 0)
# print(type(all_action))
# print(all_action)
#
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['like'] -= 1
# print(all_action)



# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan'}
# print(id(city))
# city['people'] = 32000000
# print(id(city))

# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan'}
# city['temp'] = [18, 32, 26]
# city['location'] = {'Широта': 41, 'Долгота': 69,'Высота': 500}
# print(city['location']['Широта'])
# city['size'] = 34567.45
# print(city)
# print(city['temp'][1])

# from  pprint import pprint
# pprint(city)


# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan', 'location':{'Широта': 41, 'Долгота': 69,'Высота': 500}}
# print(len(city))

# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan', }
# print(city)
#
# city.pop('name')
# print(city)
#
# del city['size']
# print(city)
#
# city.clear()
# print(city)


#
# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan', }
# city2 = city
# print(id(city))
# print(id(city2))
# city['name'] = 'London'
# print(city2)


#
# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan', }
# print(id(city))
# city2 = city.copy()
# print(id(city2))
# city['name'] = 'London'
# print(city2)


# как получить значение
# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan', }
# print(city.get('name'))
# print(city.get('name2'))

# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# if city.get('size'):
#     city['size'] = 320000
# else:
#     city['size'] = 320000
# print(city)
#
# if city.get('temp'):
#     city['temp'].append(65)
# else:
#     city['temp'] = [65]
#     print(city)


# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# print(city.get('temp',False))
# print(city.get('temp','32'))
# print(city.get('temp','Нет такого ключа'))


# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan','temp':5 }
# if 'temp' in city:
#     print('Yes')
#     print(city['temp'])
#     print(id(city))
# else:
#     print('no')

# Metods

# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# print(city.values())
# print(city.keys())
# print(city.items())

# tuple2 = ('size', 30000)
# key, value = tuple2
#
# print(key)
# print(value)

#
# key, value = ('size', 30000)
# print(key)
# print(value)


# key, value = 'size', 30000
# print(key)
# print(value)



# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# for key, value in city.items():
#     print(f'{key}:{value}')


# получение ключа от значения. готового метода нет
#
# value_intput = input('Введите значение: ')
# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# for key, value in city.items():
#     if value == value_intput:
#         print(key)



# city = {'name':'Tashkent','size': 30000, 'people': 34000000, 'country': 'Uzbekistan' }
# city2 = {'name':'Tashkent','size': 32000, 'people': 34000000, 'country': 'Uzbekistan', 'temp':[18,54,96] }
# city.update(city2)
# print(city)



# dic1 = {'name':'linux', 'automation':'bash'}
# dic2 = {'tool':'cli', 'automation':'python'}
# dic1.update(dic2)
# print(dic1)


# dic (словарь)
# hell_dict = {i:'Hello' for i in range(10) if i % 2 == 0}
# hell_dict2 = {i:'Hello' for i in range(10) if i % 2 != 0}
# hell_dict3 = {i:'Hello' for i in range(10) if i % 2 }
#
#
# print(hell_dict)
# print(hell_dict2)
# print(hell_dict3)

