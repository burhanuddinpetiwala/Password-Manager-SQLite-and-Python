from multiprocessing import connection
import sqlite3
import os

def create_dbtale():
    connection = sqlite3.connect(r"Password Manager\Password Manager\Password_Manager\User\DB\user.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS User 
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    Website CHAR(50),
                    URL TEXT(500),
                    Username CHAR(50),
                    Email TEXT(100),
                    Password TEXT(100),
                    Description TEXT(5000));''')
    
    connection.commit()
    connection.close()

def create_database():
    if os.path.exists(r"Password Manager\Password Manager\Password_Manager\User\DB"):
        if not os.path.exists(r"Password Manager\Password Manager\Password Manager\Password_Manager\User\user.db"):
            create_dbtale()
    else:
        os.mkdir(r"Password Manager\Password Manager\Password_Manager\User\DB")
        create_dbtale()

def connect_databases():
    connection = sqlite3.connect(r"Password Manager\Password Manager\Password_Manager\User\DB\user.db")
    return connection

if __name__ == "__main__":
    create_database()
