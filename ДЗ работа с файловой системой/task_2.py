'''
2.	Создайте программу, которая анализирует содержимое директории и выводит статистику: 
    1)	количество файлов
    2)	количество папок
    3)	Размер директории в мегабайтах
'''
import os

my_path = "C:\\Users\\Роман\\Downloads"


def task_2(my_path):
    sum_file = 0
    sum_folder = 0
    size_folder = os.path.getsize(my_path)/1000
    for root, dirs, files in os.walk(my_path):
        for f in files:
            sum_file += 1 # Считаем файлы

        for d in dirs:
            sum_folder += 1 # Считаем папки
    return(f"количество файлов = {sum_file}\nколичество папок = {sum_folder}\nРазмер директории в мегабайтах = {size_folder}")

print(task_2(my_path))