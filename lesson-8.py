# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).

with open("domains.txt", "r") as name:
    text = name.read()
    domen_name = text.replace(".", "")
print(domen_name)
##########################################################################
# 2.Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)

with open("names.txt", "r") as name1:
    surnames = '\n'.join([line.split()[1] for line in name1.readlines()])
print(surnames)
##########################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com

from random import randint
import random

with open("domains.txt", "r") as name:
    text = name.read()
    domen_name = text.replace(".", "")

with open("names.txt", "r") as name1:
    surnames = '\n'.join([line.split()[1] for line in name1.readlines()])

random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))

emeil = surnames + "." + str(random_number) + "@" + str(random_word) + "." + domen_name
print(emeil)

