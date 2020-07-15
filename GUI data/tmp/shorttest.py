import sqlite3

conn = sqlite3.connect('database.db')

if conn != 0:
    print("Nice PP")
else:
    print("ERROR!!!")

print(conn)
conn.close()