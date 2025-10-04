# имя пользователя, возраст, email, зарплата
from pathlib import Path
import sqlite3

db_path = "app.db"


def create_table(db_path):
    '''
    Создаёт таблицу, если её нет в базе
    '''
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()

        cur.execute(
            '''CREATE TABLE IF NOT EXISTS users(
            name TEXT,
            age INTEGER,
            email TEXT NOT NULL UNIQUE,
            sallary NUMERIC
            );
            '''
        )


def add_from_file(db_path,  file_name):
    '''
    Вставляет данные из файла в таблицу SQL
    '''
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        with open(file_name, "r", encoding="utf-8") as f:
            next(f)
            for line in f:
                cur = conn.execute(
                    '''INSERT INTO users (name, age, email, sallary)
                    VALUES (?,?,?,?)
                    ON CONFLICT(email) DO NOTHING;''',
                    (line.split(","))
                )


def calc_sum_sallary(db_path, age):
    '''
    Возвращает сумму зарплат всех пользователей до заданного количества лет
    '''
    with sqlite3.connect(db_path) as conn:
        (total,) = conn.execute(
            '''SELECT SUM(sallary)
            FROM users
            WHERE age <= ?;''',
            (age,)
        ).fetchone()
    return total


create_table(db_path)
add_from_file(db_path, "users.txt")
add_from_file(db_path, "users_new.txt")
print(calc_sum_sallary(db_path, 28))
