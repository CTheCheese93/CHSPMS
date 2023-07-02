import sqlite3

def create_injuries(connection):
    con = connection
    cur = con.cursor()

    employees = get_employees(con)