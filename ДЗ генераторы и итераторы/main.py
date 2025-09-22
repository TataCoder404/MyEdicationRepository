"""
1.	Анализ больших лог-файлов
Создайте генератор для чтения и анализа больших лог-файлов. 
Нужно найти все строки, содержащие ключевые слова "ERROR" или "WARNING" 
и вернуть их вместе с номером строки лога.

"""
# ------ Функция-генератор ------

# def iter_errors(filename):
#     with open (filename, 'r', encoding='utf-8') as file:
#         for num, line in enumerate(file):
#             if ('ERROR' in line) + ('WARNING' in line): # будем возвращать только те строки что соответствуют условию
#                 yield num, line.strip()


# for num, line in iter_errors('server.txt'): # запускаем генератор
#     print(num, line)


# ------ Генераторное выражение: структура (<результат> for <переменные> in <итерируемое> if <условие>) ------

# with open('server.txt', 'r', encoding='utf-8') as f:
#     lines = ((num, line) for num, line in enumerate(f) if ('ERROR' in line) + ('WARNING' in line))

#     for line in lines: # запускаем генератор
#         print(line)


"""
Итератор для CSV файлов
Создайте итератор для чтения первых n строк из CSV файла, 
итератор получает путь к  csv и число n – количество строк, 
которые нужно считать до закрытия файла.

"""


class ReaderIterator:
    def __init__(self, filename, n):
        self.line = 0  # текущая позиция
        self.filename = filename
        self.n = n
        self.file = None

    def __iter__(self):
        self.file = open(self.filename, "r", encoding="utf-8")
        return self

    def __next__(self):
        if self.line > self.n:
            self.file.close()
            raise StopIteration

        # вычислить текущее значение
        cur_line = self.file.readline()

        # обновить внутреннее состояние для следующего шага
        self.line += 1

        return cur_line


for i in ReaderIterator("pizza_v1.csv", 5):
    print(i)
