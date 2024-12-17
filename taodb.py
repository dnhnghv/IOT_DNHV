import sqlite3

conn = sqlite3.connect('db_test.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS sense_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hum  REAL NOT NULL,
    temp REAL NOT NULL
)
''')

print("tao csdl thanh cong")