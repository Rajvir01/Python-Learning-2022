import mysql.connector as db

class DataBaseHelper:

    def __init__(self, database='cmsapp'):
        self.connection = db.connect(user='root', password='bansal12',
                                     host='127.0.0.1',
                                     database=database)
        print("1. DATABASE CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("2. CURSOR CONNECTED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY CREATED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

