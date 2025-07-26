# 1. Дан список [1, 2, 3, 4]. Создайте новый список с квадратами чисел.

# list = [1,2,3,4]
# new_list = []

# for i in list:
#     new_list.append(i**2)

# print(new_list)

# 2. Дан список [1, 2, 3, 4, 5, 6]. Оставьте только чётные числа.

# list = [1, 2, 3, 4, 5, 6]
# new_list = []

# for i in list:
#     if i % 2 == 0:
#         new_list.append(i)

# print(new_list)

# 3. Дан список строк ["hello", "world"]. Сделайте все буквы заглавными.

# list = ["hello", "world"]
# new_list = []

# for i in list:
#     new_list.append(i.upper())

# print(new_list)

# 4.Даны списки [1, 2, 3] и [4, 5, 6]. Перемножьте их поэлементно.

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# new_list = []

# for i in list_1:
#     for j in list_2:
#         if list_1.index(i) == list_2.index(j):
#             new_list.append(i*j)

# print(new_list)

# 5 Дан список ["a", "abc", "abcd", "xyz"]. Оставьте строки длиннее 3 символов.

# list = ["a", "abc", "abcd", "xyz"]
# new_list = []

# for i in list:
#     if len(i) > 3:
#             new_list.append(i)

# print(new_list)

# 6. Дан список [1, 2, 3, 4, 5]. Найдите сумму квадратов чётных чисел.

# list = [1, 2, 3, 4, 5, 6]
# sum = 0

# for i in list:
#     if i % 2 == 0:
#         sum += i

# print(sum)

# 7. Дана строка "a1b2c3". Извлеките цифры и преобразуйте их в числа.

# my_str = "a1b2c3"
# list = []

# for i in my_str:
#     try:
#         int(i)
#         list.append(i)
#     except:
#         pass

# print(list)

# 8. Дан список ["apple", "banana", "cherry"]. Получите список длин.

# list = ["apple", "banana", "cherry"]
# list_len = []

# for i in list:
#     list_len.append(len(i))

# print(list_len)

# 9. Дан список [-1, 2, -3, 4, -5]. Оставьте только положительные числа.

list = [-1, 2, -3, 4, -5]
new_list = []

for i in list:
    if int(i) > 0:
        new_list.append(i)

print(new_list)