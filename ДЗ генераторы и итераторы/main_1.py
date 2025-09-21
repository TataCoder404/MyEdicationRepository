# def chet(n):
#     for i in range(2, n, 2):
#         yield i
#
#
# for i in chet(5):
#     print(i)



class Fibo:
    def __init__(self, n):
        self.pred1 = 0
        self.pred2 = 1
        self.n = n
        self.cur = 0
        self.db = None

    def __iter__(self):
        return self


    def __next__(self):
        res = self.pred1
        self.pred1, self.pred2 = self.pred2, self.pred1 + self.pred2
        self.cur += 1
        if self.n < self.cur:
            raise StopIteration
        return res

# 0 1 1 2 3 5 8 13


def gen_fibo(n):
    pred1 = 0
    pred2 = 1
    res = pred1
    for i in range(n):
        res = pred1
        pred1 = pred2
        pred2 += res
        yield res

import sqlite3
class Films_iter:
    def __init__(self, database, table, rows, offset, **kwargs):
        self.db = database
        self.table_name = table
        self.rows = rows
        self.offset = offset
        self.cur = 0
        self.data_len = 0
        self.connect = None
        self.curs = None
        self.data = None
        self.params = kwargs  # {genre: "вестерн"}

    def __iter__(self):
        self.connect = sqlite3.connect(self.db)
        self.curs = self.connect.cursor()
        if self.params:
            if len(self.params) == 1:
                sql = f"""SELECT * FROM {self.table_name} WHERE {list(self.params.keys())[0]} = ? LIMIT ? OFFSET ?"""
                self.data = self.curs.execute(sql, (*self.params.values(), self.rows, self.offset))
            else:
                numeric = {}
                strings = {}
                for key, value in self.params.items():
                    if isinstance(value, str):
                        strings[key] = value
                    else:
                        numeric[key] = value

                sql_stings = " AND ".join([f"{str(key)} = ?" for key in strings])
                sql_numeric = " AND ".join([f"{str(key)} > ?" for key in numeric])
                sql_all = " AND ".join([sql_stings, sql_numeric])
                sql = f"""SELECT * FROM {self.table_name} WHERE {sql_all} LIMIT ? OFFSET ?"""
                print(sql)
                self.data = self.curs.execute(sql, (*strings.values(), *numeric.values(), self.rows, self.offset))
        else:
            sql = f"""SELECT * FROM {self.table_name} LIMIT ? OFFSET ?"""
            self.data = self.curs.execute(sql, (self.rows, self.offset))

        self.data = self.data.fetchall()
        self.data_len = len(self.data)
        return self

    def __next__(self):
        if self.cur == self.data_len:
            self.connect.close()
            self.cur = None
            self.data = None
            raise StopIteration
        res = self.data[self.cur]
        self.cur += 1
        return res


films = Films_iter("movies.db", "movies", 999, 1, genre="Вестерн", year=2000, rating=8)
for i in films:
    print(i)
