# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def summ_ele(list):
#     summ = 0
#     for i in range(1,len(list),2):
#         summ += list[i]
#     return summ
# a = [2, 3, 5, 9, 3, 10]
# print(summ_ele(a))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def comp_ele(list):
#     comp = 1
#     last_ele = len(list) -1
#     for i in range(0,len(list)):
#         if i - last_ele == 1:
#             break
#         elif i != last_ele:
#             comp = list[i] * list[last_ele]
#             last_ele -= 1
#             print(comp)
#         elif i == last_ele:
#             comp = list[i]**2
#             print(comp)
#             break
# a = [2, 3, 4, 5, 6, 8, 10, 2, 5]
# comp_ele(a)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def diff_ele(list):
#     minn = 1
#     maxx = 0     
#     for i in list:
#         if (i - int(i)) <= minn:
#             minn = i - int(i)
#         if (i - int(i)) >= maxx:
#             maxx = i - int(i)  
#     print(maxx-minn)
# a = [1.1, 1.2, 3.1, 10.01]
# diff_ele(a)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def translation(a):
#     my_list = []
#     b = 0
#     while a != 0:
#         b = a % 2
#         a = a // 2
#         my_list.insert(0, b)
#     print(*my_list, sep = '')
# k = 2
# translation(k)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fibb_find(k):
#     if k in [1,2]:
#         return 1
#     else:      
#         return fibb_find(k-1) + fibb_find(k-2)
# list = []
# a = 10
# for i in range(1, a+1):
#     list.append(fibb_find(i))
#     if i % 2 == 0:
#         list.insert(0,fibb_find(i)*-1)
#     else:
#         list.insert(0,fibb_find(i))
# print(list)
