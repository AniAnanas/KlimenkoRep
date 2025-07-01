print("[Program started]")
"""Вариант 13.
Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных
запасов на складе. БД должна содержать таблицу Товары со следующей структурой
записи: Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный
запас.
"""
from os import path
from typing import Any
import sqlite3


class Tovar:
    def __init__(self, marka: str, type: str, price: float|int, count: int, min_count: int, id: int=-1):
        self.id = id
        self.marka = marka
        self.type = type
        self.price = price
        self.count = count
        self.min_count = min_count

    def change_price(self, price: float|int):
        self.price = price
        return self

    def change_count(self, count: int):
        self.count = count
        return self
    
    def unpack(self):
        return self.marka, self.type, self.price, self.count, self.min_count

    def __str__(self):
        return f"ID: {self.id}, Марка: {self.marka}, "+\
            f"Тип: {self.type}, Цена: {self.price}, "+\
            f"Количество: {self.count}, Минимальный запас: {self.min_count}"

class DB:
    def __init__(self, db_name:str='tovarniy_zapas.db'):
        self.db_name = db_name
        self.check_table()
        self.columns = ["id", "marka", "type", "price", "count", "min_count"]
        
    def check_table(self):
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()
            try:
                curs.execute("select id, marka, type, price, count, min_count from tovars")
            except sqlite3.OperationalError:
                curs.execute("""CREATE TABLE IF NOT EXISTS tovars (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marka TEXT,
                    type TEXT,
                    price REAL,
                    count INTEGER,
                    min_count INTEGER )""")
                con.commit()
                print("[Table tovars created]")
    
    def add_tovar(self, tovar: Tovar):
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()
            curs.execute(
                "INSERT INTO tovars (marka, type, price, count, min_count) \
                    VALUES (?, ?, ?, ?, ?)",
                tovar.unpack()
            )
            con.commit()
        print(f"[Tovar {curs.lastrowid} added]")
        return curs.lastrowid
    
    def add_many_tovars(self, tovars: list[Tovar], return_ids: bool=False):
        params = [(tovar.marka, tovar.type, tovar.price, tovar.count, tovar.min_count) for tovar in tovars]
        result = []
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()
            if return_ids:
                for param in params:
                    curs.execute("""INSERT 
                        INTO tovars (marka, type, price, count, min_count) 
                        VALUES (?, ?, ?, ?, ?)""", 
                        param
                    )
                    result.append(curs.lastrowid)
            else:
                curs.executemany("""INSERT 
                    INTO tovars (marka, type, price, count, min_count) 
                    VALUES (?, ?, ?, ?, ?)""", 
                    params
                )

            con.commit()
        print(f"[{len(tovars)} Tovars added]")
        return result
    
    def delete_tovar(self, id):
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()

            curs.execute("DELETE FROM tovars WHERE id = ?", (id,))

            msg = "DELETE>> [Tovar {0} "
            if curs.rowcount > 1:
                msg += "deleted, but more than 1 - {1}]"
            elif curs.rowcount == 1:
                con.commit()
                msg += "deleted]"
            elif curs.rowcount == 0:
                msg += "not found]"
            else:
                msg += "not deleted idk why]"
            print(msg.format(id, curs.rowcount))
    
    def update_tovar(self, id, tovar: Tovar):
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()

            curs.execute(
                "UPDATE tovars SET marka = ?, type = ?, price = ?, count = ?, min_count = ? \
                 WHERE id = ?",
                 (*tovar.unpack(), id))
            
            msg = "UPDATE>> [Tovar {0} "
            if curs.rowcount > 1:
                msg += "updated, but more than 1 - {1}]"
            elif curs.rowcount == 1:
                con.commit()
                msg += "updated]" 
            elif curs.rowcount == 0:
                msg += "not found]"
            else:
                msg += "not updated idk why]"

            print(msg.format(id, curs.rowcount))

    def find_tovar(self, key: str="id", value: Any=0):
        with sqlite3.connect(self.db_name) as con:
            curs = con.cursor()
            curs.execute(f"SELECT * FROM tovars WHERE {key} = ?", (value,))
            row = curs.fetchone()

            if row:
                tovar = Tovar(*row[1:], row[0])
                print(f"FIND>> [{tovar}]")
                return tovar
            else:
                print(f"FIND>> [Tovar with {key} = {value} not found]")
                return None


def main(db_name):
    try:
        db = DB(db_name)
        db.add_tovar(Tovar("LG", "Телевизор", 50_000, 10, 5))
        db.add_tovar(Tovar("Samsung", "Телевизор", 60_000, 5, 3))
        db.add_many_tovars([
            Tovar("Sony", "Телевизор", 70_000, 8, 6),
            Tovar("Xiaomi", "Планшет", 30_000, 15, 10),
            Tovar("Apple", "Планшет", 40_000, 12, 8),
            Tovar("Huawei", "Телефон", 20_000, 20, 15),
            Tovar("Google", "Телефон", 25_000, 18, 12),
            Tovar("Sony", "Наушники", 15_000, 25, 20),
            Tovar("JBL", "Наушники", 18_000, 22, 18),
            Tovar("Bose", "Наушники", 20_000, 19, 15)
        ])
        first = db.find_tovar("id", 1)
        if first:
            db.update_tovar(first.id, first.change_price(65_000))
            db.delete_tovar(first.id)

        second = db.find_tovar("marka", "Xiaomi")
        if second:
            db.update_tovar(second.id, second.change_count(20))
            db.delete_tovar(second.id)
        
        third = db.find_tovar("type", "Телевизор")
        if third:
            db.update_tovar(third.id, third.change_price(55_000))
            db.delete_tovar(third.id)
        

    except sqlite3.Error as e:
        print(f"[DB Error: {e}]")
        return 1
    except Exception as e:
        print(f"[Error: {e}]")
        return 1
    return 0

if __name__ == "__main__":
    my_path = path.join(path.dirname(__file__), "tovarniy_zapas.db")
    print(my_path)
    exit(main(my_path))