values = 23423342589098
my_symbol = "0"

count = values.count(my_symbol)
print(count)

################################################################################

value = 65767760000
count = 0
while value % 10 == 0:
   count += 1
   value //= 10
print(count)

################################################################################

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for value in my_list_1:
   if value % 2 == 0:
       my_result.append(value)

for value in my_list_2:
   if value % 2 == 1:
       my_result.append(value)

print(my_result)

################################################################################

my_list = [1, 2, 3, 4, 5]
new_list = []

for symbol in my_list:
   if symbol not in new_list:
       new_list.append(symbol)

new_list.append(new_list[0])
new_list.pop(0)
print(new_list)

################################################################################

my_list = [1, 2, 3, 4, 5]

my_list.append(my_list[0])
my_list.pop(0)
print(my_list)


################################################################################

my_str = '43 больше чем 34 но меньше чем 56'
new_str = my_str.split()
my_list = []


for index in new_str:
   if index.isdigit() == True:
       my_list.append(int(index))

print(sum(my_list))

################################################################################
import re
my_str = 'qwerrrtyu'
my_str_2 = '_'

if len(my_str) % 2 == 1:
   my_str = my_str + my_str_2

items = re.findall(r'.{1,2}', my_str )

print(items)

################################################################################

my_str = "My_long string"
l_limit = "o"
r_limit = "t"
sub_str = []

index_l = my_str.find(l_limit)+1
index_r = my_str.find(r_limit)
sub_str = my_str[index_l:index_r]

print(sub_str)

################################################################################

my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []

index_l = my_str.find(l_limit)+1
index_r = my_str.rfind(r_limit)
sub_str = my_str[index_l:index_r]


print(sub_str)


################################################################################

a = [2,4,1,5,3,9,0,7]
counter = 0
for i in range(1, len(a) - 1):
 if a[i - 1] < a[i] > a[i + 1]:
   counter += 1
print(counter)