# ---------------------- 1 ---------------------------

# def politeFunction():
#     name = ''
#     text = ''

#     if name == '':
#         name = input('Введите имя: ')
#     if name != '':
#         text = input(f'{name}, введите текст: ')

#     return print(f'{name}, Вы ввели: {text}')

# politeFunction()


# ---------------------- 2 ---------------------------

# text = ''

# def parrot():
#     global text
#     if text == '':
#         text = input('Введите текст: ')
#     else:
#         print(text)


# parrot()
# parrot()
# parrot()


# ---------------- альтернатива без global --------------------------
# class Parrot:
#     def __init__(self):
#         self.text = ''

#     def say(self):
#         if not self.text:
#             self.text = input('Введите текст: ')
#         else:
#             print(self.text)

# parrot = Parrot()
# parrot.say()
# parrot.say()
# parrot.say()

# ---------------------- 3 ---------------------------

# list_of_friends = {}

# # Функция add_friends(person, friends) принимает на вход два аргумента: имя человека и список имен его друзей и добавляет связку в словарь.

# def add_friends(person, friends):
#     list_of_friends[person] = friends


# add_friends('Anna', ['Kirill', 'Oleg', 'Tata'])
# add_friends('Marina', ['Sasha', 'Roman', 'Gretta', 'Oleg'])

# print(list_of_friends)

# # Функция are_friends(person1, person2) принимает на вход два аргумента: имя первого человека и имя второго человека и 
# # возвращает True или False, в зависимости от того, считает ли первый человек второго своим другом.

# def are_friends(person1, person2):

#     if person1 in list_of_friends:
#         result = list_of_friends.get(person1)
#         if person2 in result:
#             return True
#         else:
#             return False
#     else:
#         print(f'{person1} не найден в списке твоих друзей')


# print(are_friends('Anna', 'Oleg'))

# # Функция print_friends(name_of_person) принимает на вход имя человека и печатает список его друзей через пробел в алфавитном порядке.

# def print_friends(name_of_person):

#     # Ищем name_of_person в ключах:
#     if name_of_person in list_of_friends:
#         result = list_of_friends.get(name_of_person)
#         result.sort()
#         print(result)

#     # Ищем name_of_person в значениях (во всех списках друзей):
#     matching_keys = []

#     for key, values in list_of_friends.items():  # перебираем словарь (key — это текущий ключ; values — это список, который является значением этого ключа.)
#         if name_of_person in values:
#             matching_keys.append(key)

#     print(matching_keys)

# print_friends('Oleg')

# ---------------------- 4 ---------------------------

# Напишите функцию bet() для совершения ставок, которая первым аргументом принимает номер лошади, а вторым ставку. 
# Лошади пронумерованы от 1 до 10. На одну и ту же лошадь нельзя сделать ставку дважды. Также нельзя делать нулевую ставку.

# bets = {}

# def bet(horse, rate):

#     if not 1 <= horse <= 10:
#         print(f'Ошибка. Ставка не принята, указан неверный номер лошади. Вы указали {horse}')
#         return False

#     if horse in bets:
#         print(f'Ошибка. Ставка не принята, Вы уже ставили на эту лошадь. Вы указали {horse}. Ваша ставка: {rate}')
#         return False

#     if rate <= 0:
#         print(f'Ошибка. Ставка не принята, нельзя делать нулевую ставку. Ваша ставка: {rate}')
#         return False

#     bets[horse] = rate
#     print(f'Ставка сделана. Лошадь: {horse}, Ставка: {rate}')
#     return True

# bet(0, 4)
# bet(1, 0)
# bet(4, 300)

# print(bets)

