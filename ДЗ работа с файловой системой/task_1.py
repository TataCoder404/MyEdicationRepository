'''Напишите функцию, которая находит все файлы с определенным расширением в указанной директории и ее поддиректориях. 
Функция принимает путь, где нужно искать и расширение, выводит подходящие файлы.
'''
import os

my_path = "C:\\Users\\Роман\\Downloads"
file_extension = ".xlsx"

def seach_file(my_path, file_extension):
    if os.path.isdir(my_path):
        for root, dirs, files in os.walk(my_path):
            for name in files:
                root, ext = os.path.splitext(name)
                if ext == file_extension:
                    print(root)


seach_file(my_path, file_extension)