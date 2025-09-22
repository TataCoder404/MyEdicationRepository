'''
2.	Создайте итератор чисел, являющихся квадратами целых чисел. 
Итератор принимает диапазон a, b и выдает числа от a до b, которые являются квадратами целых чисел.
'''


# class SqrtIterator:
#     def __init__(self, a, b):
#         self.a = int(a)
#         self.b = int(b)
#         self.current = self.a

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.current <= self.b:
#             i = self.current
#             self.current += 1
#             r = int(i ** 0.5)
#             if r * r == i:
#                 return i
#         raise StopIteration


# for j in SqrtIterator(15, 30):
#     print(j)


"""
3.	Создайте filter из итератора. 
Принимает функцию и итерируемый объект, возвращает значения из итерируемого объекта, 
которые дают True при применении к ним функции.
"""
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []


# def is_even(x):
#     return x % 2 == 0


# class FilterIterator:
#     def __init__(self, func, my_obj):
#         self.index = 0  # пример: текущая позиция
#         self.my_obj = my_obj
#         self.func = func

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.index > len(self.my_obj):
#             # обращение к элементу списка по индексу
#             value = self.my_obj[self.index]
#             self.index += 1
#             if self.func(value):
#                 return value
#         raise StopIteration


# it = FilterIterator(is_even, list)

# for i in it:
#     print(i)


"""
4.	Создайте итератор, который пишет числа от числа x и по возрастанию ровно n секунд.
"""

# import time
# class CounterIterator:
#     def __init__(self, x, n):
#         self.current = 0  # пример: текущая позиция
#         self.start = None
#         self.n = n
#         self.x = x

#     def __iter__(self):
#         self.start = time.time()
#         return self

#     def __next__(self):
#         if self.current >= self.x:
#             print("Все числа выведены")
#             raise StopIteration

#         if time.time() - self.start >= self.n:
#             print("Время вышло")
#             raise StopIteration

#         self.current += 1

#         return self.current


# for i in CounterIterator(100000000, 5):
#     print(i)


"""
5.	Прочитайте итератором все четные строки txt файла.
"""


class ReaderTxt:
    def __init__(self, filename):
        self.index = 0
        self.filename = filename
        self.file = None

    def __iter__(self):
        self.file = open(self.filename, "r", encoding="utf-8")
        return self

    def __next__(self):
        while True:

            line = self.file.readline()

            if not line:
                self.file.close()
                raise StopIteration

            self.index += 1

            if self.index % 2 == 0:
                return line.strip()


for i in ReaderTxt("pizza_v1.csv"):
    print(i)
