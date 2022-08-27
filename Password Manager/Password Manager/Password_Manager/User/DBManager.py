from multiprocessing import connection
import sqlite3
from UserDB import connect_databases
from prettytable import PrettyTable

def store_password(Website, URL, Username, Email, Password, Description):

    connection = connect_databases()
    cursor = connection.cursor()

    sqlQuery = "INSERT INTO User (Website, URL, Username, Email, Password, Description) VALUES (?, ?, ?, ?, ?, ?)"
    value = (Website, URL, Username, Email, Password, Description)

    cursor.execute(sqlQuery, value)

    connection.commit()
    connection.close()

def delete_password(ID):

    connection = connect_databases()
    cursor = connection.cursor()

    sqlQuery = "DELETE FROM User WHERE ID = ?"
    entry_to_del = (ID,)

    cursor.execute(sqlQuery, entry_to_del)
    connection.commit()
    connection.close()

    print("Record with {} deleted successfully.".format(ID))

def show_details():

    connection = connect_databases()
    cursor = connection.cursor()

    sqlQuery = "SELECT Website, URL, Username, Email, Description from User"
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()
    
    Table = PrettyTable(["Website", "URL", "Username", "Email", "Description"])

    for row in rows:
        Table.add_row(row)
    print(Table)


show_details()
