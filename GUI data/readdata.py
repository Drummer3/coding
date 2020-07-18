import sqlite3

class fillArr:
    def __init__():
        arr = []
        try:
            con = sqlite3.connect("database.db")
            read_table(con)
        except sqlite3.Error as e:
            print(e)
    def read_table(con):
        cur = con.cursor()
        cur.execute("SELECT * FROM List")

        rows = cur.fetchall()

        for row in rows:
            arr.append(row)
        return arr