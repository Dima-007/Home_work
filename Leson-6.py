
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.


my_list = ["car", "cat", "dog", "red", "apple"]
my_list_2 = []

for index, item in enumerate(my_list):
    if index % 2 != 0:
        my_list_2.append(item[::-1])
    else:
        my_list_2.append(item)
print(my_list_2)
#################################################################

#2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".


my_list = ["car", "cat", "dog", "red", "apple"]
new_list =[]

for value in my_list:
    if value[0] == "a":
        new_list.append(value)

print(new_list)
#################################################################

#3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.


my_list = ["car", "cat", "dog", "red", "apple"]
new_list = [new_list for new_list in my_list if "a" in new_list]
print(new_list)
#################################################################

#4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.


my_list = ["one", "two", "list", "dict", 100, 1, 50]
new_list = []
for value in my_list:
   if isinstance(value, str):
       new_list.append(value)
#################################################################

#5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.


my_str = "ss", "rr", "jj", "rr", "gg"
my_list = []
result = set([symbol for symbol in my_str if my_str.count(symbol) == 1])

for value in result:
    if value not in my_list:
        my_list.append(value)
print(my_list)
#################################################################

#6. Даны две строки. Создать список в который поместить те символы,
# кторые есть в обеих строках хотя бы раз.


my_list = "a", "b", "f", "h", "g", "k", "s"
my_list_2 = "a", "b", "f", "h", "t", "n", "l"
result = [elem for elem in my_list if elem in my_list_2]
print(result)
#################################################################

#7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


my_str_1 = "one", "two", "list", "car", "car"
my_str_2 = "one", "list", "two", "car", "car"
my_1 = set([symbol for symbol in my_str_1 if my_str_1.count(symbol) == 1])
my_2 = set([symbol for symbol in my_str_2 if my_str_2.count(symbol) == 1])
result = list(my_1. intersection(my_2))
print(result)








