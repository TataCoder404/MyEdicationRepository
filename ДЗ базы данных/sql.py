import sqlite3

conn = sqlite3.connect("bd.db")
curs = conn.cursor()
try:
    curs.execute("""CREATE TABLE [table] (
        number INTEGER
    );""")
    conn.commit()
except Exception as e:
    print(e)

# 5
# 6
# 7
while True:
    print("1 - SELECT")
    print("2 - INSERT")
    print("3 - UPDATE")
    print("4 - DELETE")
    req = int(input())
    if req == 1:
        req = input("Запрос:")
        x = int(input("критерий:"))
        data = curs.execute(req, (x, ))
        print("результат запроса")
        for i in data:
            print(i)
    if req == 2:
        req = """INSERT INTO [table](number) VALUES(?)"""
        num = input("Число:")
        data = curs.execute(req, (num,))
        conn.commit()

    if req == 3:
        req = input("Запрос:")
        x = int(input("критерий:"))
        data = curs.execute(req, (x,))
        conn.commit()

    if req == 4:
        req = input("Запрос:")
        num = input("Число:")
        data = curs.execute(req, (num,))
        conn.commit()

    print("таблица:")
    data = curs.execute("SELECT * FROM [table]").fetchall()
    for i in data:
        print(i)
