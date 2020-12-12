# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
#
# from random import randrange as r
# for _ in range(20):
#     print(r(0, 100))
#######################################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

# import random as r
# triangle = {key: tuple(r.randint(-10, 10) for _ in range(2)) for key in "ABC"}
# print("triangle", triangle)
#######################################################################

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

# my_str = "I'm the string"
# def func (a, b):
#     return a + my_str + b
# print(func('***', '***'))
#######################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

# persons = [{"name": "John", "age": 15},
#            {"name": "Sasha", "age": 20},
#            {"name": "Vlad", "age": 30},
#            {"name": "Ira", "age": 30}
#            ]
# min_age = min(person["age"] for person in persons)
# for a in persons:
#     if a["age"] == min_age:
#         print(a)
#######################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

# persons = [{"name": "John", "age": 15},
#            {"name": "Sasha", "age": 20},
#            {"name": "Vlad", "age": 30},
#            {"name": "Ira", "age": 30}
#            ]
# max_name = max(len(person["name"]) for person in persons)
# for a in persons:
#     if len(a["name"]) == max_name:
#         print(a)
#######################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# в) Посчитать среднее количество лет всех людей из списка.

# persons = [{"name": "John", "age": 15},
#            {"name": "Sasha", "age": 20},
#            {"name": "Vlad", "age": 30},
#            {"name": "Ira", "age": 30}
#            ]
# sum_age = sum(person["age"] for person in persons)/len(persons)
# print("sum_age", sum_age)
#######################################################################

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

# my_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# my_dict_2 = {"t": 1, "b": 2, "e": 5, "c": 3}
# dict_key = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
# print("dict_key", dict_key)
# print("dict_key &:", list(my_dict_1.keys() & my_dict_2.keys()))
# print("dict_key &:", list(my_dict_2.keys() & my_dict_1.keys()))
#######################################################################

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# my_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# my_dict_2 = {"t": 1, "b": 2, "e": 5, "c": 3}
# difference_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
# print("difference_keys", difference_keys)
#######################################################################

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# my_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# my_dict_2 = {"t": 1, "b": 2, "e": 5, "c": 3}
# difference_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
# new_dict = {key: my_dict_1[key] for key in difference_keys}
# print(new_dict)

#######################################################################

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

# my_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# my_dict_2 = {"t": 1, "b": 2, "e": 5, "c": 3}
# intersection_keys = list(my_dict_2.keys() & my_dict_1.keys())
# unique_keys_in_dicts = list(my_dict_1.keys() ^ my_dict_2.keys())
# print("unique_keys_in_dicts", unique_keys_in_dicts)
#
# unique_dict1 = {key:  value for key, value in my_dict_1.items() if key in unique_keys_in_dicts}
# print("unique_dict1", unique_dict1)
# unique_dict2 = {key:  value for key, value in my_dict_2.items() if key in unique_keys_in_dicts}
# print("unique_dict1", unique_dict2)
# common_keys_dict ={kay: [my_dict_1[kay], my_dict_2[kay]] for kay in intersection_keys}
# print("common_keys_dict", common_keys_dict)
# merge_dict = {**unique_dict1, **unique_dict2, **common_keys_dict}
# print("merge_dict", merge_dict)