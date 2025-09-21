'''
2.	Создайте итератор чисел, являющихся квадратами целых чисел. 
Итератор принимает диапазон a, b и выдает числа от a до b, которые являются квадратами целых чисел.
'''


class SqrtIterator:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.current = self.a

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.b:
            i = self.current
            self.current += 1
            r = int(i ** 0.5)
            if r * r == i:
                return i
        raise StopIteration


for j in SqrtIterator(15, 30):
    print(j)
