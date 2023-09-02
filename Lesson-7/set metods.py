# set1 = {100, 12, 23, 34, 56}
# print(set1)
# list1 = list(set1)
# print(list1)


# Без сета (set)
# list1 = [12, 23, 34, 12, 34,12]
# list2 =[]
# for i in list1:
#     if not i in  list2:
#         list2.append(i)
# print(list2)

# C сетом (set)
# list1 = [12, 23, 34, 12, 34,12]
# list2 =list(set(list1))
# print(list2)


# set1 = {100, 12, 23, 34, 56}
# print(set1)
# set1.add(200) #добавляет указанный элемент
# print(set1)
# set1.remove(100) #удаляет указанный элемент
# print(set1)
# temp = set1.pop()    #удаляет 1 элемент
# print(set1)
# print(temp)


#
# set1 = {100, 12, 23, 34, 56}
# set2 = {200, 12, 23, 34, 56}
# set1.update(set2)
# print(set1)


# domain = ['olx.uz', 'distro.uz', 'olx.uz', 'ya.ru']
# domain = list(set(domain))
# print(domain)

## intersection () - пересичения
# set1 = {1, 2, 3, 4}
# set2 = {2,3 ,6}
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1 & set2
# print(set3)

## difference() -
# set1 = {1, 2, 3, 4}
# set2 = {2,3 ,6}
# set3 = set1.difference(set2)
# print(set3)
# set3 = set1 - set2
# print(set3)


## symetric difference () - уникальные
# set1 = {1, 2, 3, 4}
# set2 = {2,3 ,6}
# set3 = set1.symmetric_difference(set2)
# print(set3)
# set3 = set1 ^ set2
# print(set3)

##union() -
# set1 = {1, 2, 3, 4}
# set2 = {2,3 ,6}
# set3 = set1.union(set2)
# print(set3)
# set3 = set1 | set2
# print(set3)


