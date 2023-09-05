# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
n = int(input("введите количество элементов списка: "))
list1 = [randint(0, 20) for i in range(n)]
print(list1)
min = int(input("введите минимальное значение: "))
max = int(input("введите максимальное значение: "))
list2 = []
for i in range(len(list1)):
    if list1[i] > min and list1[i] < max:
        list2.append(i)
print(list2)