import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root', password='bansal12',
                                     host='127.0.0.1',
                                     database='rajvir')
        print("Database Connected :)")
        self.cursor = self.connection.cursor()
        print("Cursor CREATED :)")

    def write(self):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED:)")

    def read(self):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows