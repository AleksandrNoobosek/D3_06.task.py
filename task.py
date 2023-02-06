"""Создайте список из случайных чисел. Найдите количество различных элементов в нем"""

# import random
# el_list = [random.randint(1,10) for _ in range(10)]
# print(f'Наш список: {el_list}')
# various = set(el_list)
# print(f'Количество различных элементов: {various}')

""" Фрукты.Пользователь вводит число K - количество фруктов. 
Затем он вводит K фруктов в формате: название фрукта и его количество. 
Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. """

# finish_list = {}
# k = int(input('Количество фруктов ==> '))
# for i in range(0, k):
#     fruit = input('название фрукта ==> ')
#     quantity = input('количество ==> ')
#     finish_list[fruit] = quantity
# print(f'Результат ==> {finish_list}')

""" Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
Создайте список friends и добавьте в него N словарей с ключами name и age.
Найдите самого младшего из друзей и выведите его имя. """

# n = int(input('Количество друзей ==> '))
# friends = []
# for el in range(n):
#     new_dict = {}
#     name = input('Имя друга ==> ')
#     age = int(input('Возраст друга ==> '))   
#     new_dict[name] = age
#     friends.append(new_dict)
#"""  print(*friends) """

# minn_list = []
# i = 0
# while i < len(friends):
#     for el in friends[i]:
#         minn_list.append(friends[i][el])        
#     i += 1

# for i in friends[minn_list.index(min(minn_list))]:
#     result = i
# print (f'Самый младший ==> {result}')


""" 3. Еще немного о друзьях. Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) 
своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. 
Выведите средний возраст всех друзей и самое длинное имя. """

# n = int(input('Количество друзей ==> '))
# friends = []
# n_list = []
# a_list = []
# for el in range(n):
#     new_dict = {}
#     name = input('Имя друга ==> ')
#     age = int(input('Возраст друга ==> '))   
#     new_dict[name] = age
#     friends.append(new_dict)
#     n_list.append(name)
#     a_list.append(age)

# maxx_symbol = n_list[0]
# for el in range(len(n_list) - 1):
#     if len(n_list[el + 1]) > len(n_list[el]):
#         maxx_symbol  = n_list[el + 1]

# summ_age = 0
# for el in a_list:
#     summ_age += el

# result_age = summ_age/len(a_list)

# print(f'Cамое длинное имя ==> {maxx_symbol}')  
# print(f'Средний возраст ==> {result_age}')


""""Пора учить английский язык", - сказал себе Степа и решил написать программу 
для изучения английского языка. Программа получает на вход слово на английском языке 
и несколько его переводов на русском языке. Составьте словарь, 
в котором ключ - это английское слово, а значение - это список русских слов. 
В этой задаче нужно использовать строчный метод split()."""

# n = int(input('Количество слов ==> '))
# dictionary = {}
# for i in range(n):
#     name = input('Введите слово ==> ')
#     age = input('Перевод==> ').split()
#     dictionary[name] = age
# print(dictionary)
