from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('user_table.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
(user_id INTEGER PRIMARY KEY, first_name Text, Last_name Text, Email_address Text)
''')

User_insert = [('Burhanuddin', 'Petiwala', 'burhanuddinpetiwala@gmail.com'), ('Burhan', 'Petiwala', 'burhanuddinpetiwalaCanada@gmail.com')]

cursor.executemany('''INSERT INTO Users (first_name, Last_name, Email_address) VALUES (?,?,?)''',User_insert)

cursor.execute('''SELECT * FROM Users''')
print(cursor.fetchall())

connection.commit()
connection.close()
