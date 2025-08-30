'''
3.	Напишите программу, которая организует файлы в указанной директории по их расширениям, 
создавая соответствующие папки и перемещая туда файлы.
'''

import os

my_path = "C:\\Users\\Роман\\Downloads"

def seach_file(my_path):
    for root, dirs, files in os.walk(my_path):
        for name in files:
            _, ext = os.path.splitext(name)

            src = os.path.join(root, name) # исходный путь
            if ext == "":
                folder_for_file = f"{my_path}\\расширение_нет"
            else:
                folder_for_file = f"{my_path}\\расширение {ext}" # новая папка с названием расширения

            dst = os.path.join(folder_for_file, name) # конечный путь (папка + файл)
            if os.path.exists(folder_for_file):
                os.replace(src, dst)
            else:
                os.mkdir(folder_for_file)
                os.replace(src, dst)
    return(print("Я всё!"))

seach_file(my_path)