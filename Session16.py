"""
    Principle of OOPS

        Crossing
            name, latitude, longitude, status, personInCharge

        HealthLogger
            phone, weight, bp, sugar, logTimeStamp

        VegetableSeller
            name, phone, amount, logTimeStamp, description, frequency

        create table healthlogger(
            id int primary key auto_increment,
            phone varchar(10),
            weight int,
            bp_high int,
            bp_low int,
            sugar int,
            log_time_stamp datetime
        );
"""

import datetime
import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root', password='bansal12',
                                     host='127.0.0.1',
                                     database='HealthLogger')
        print("DB CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


class HealthLogger:

    db_helper = DBHelper()

    def save_log(self):
        self.id = None
        self.phone = input("Enter Phone Number: ")
        self.weight = input("Enter Weight: ")
        self.bp_high = input("Enter BP High: ")
        self.bp_low = input("Enter BP Low: ")
        self.sugar = input("Enter Diabetes: ")
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "insert into HealthLogger values(null, '{phone}', " \
              "{weight}, {bp_high}, {bp_low}, {sugar}, " \
              "'{log_time_stamp}')".format_map(vars(self))
        print(sql)

        save = input("Do you wish to Save the Record (yes/no)")
        if save == "yes":
            self.db_helper.write(sql)


    def update_log(self):
        self.id = int(input("Enter Log ID: "))
        self.phone = int(input("Enter Phone Number: "))
        self.weight = int(input("Enter Weight: "))
        self.bp_high = int(input("Enter BP High: "))
        self.bp_low = int(input("Enter BP Low: "))
        self.sugar = int(input("Enter Diabetes: "))
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

        sql = "update HealthLogger set" , \
              "phone = '{phone}', " \
              "weight = {weight}," \
              "bp_high = {bp_high}, bp_low = {bp_low}, " \
              "sugar = {sugar}, log_time_stamp = '{log_time_stamp}' " \
              "where id = {id}".format_map(
            vars(self))

        print(sql)

        update = input("Do you wish tio update the Record (yes/no)")
        if update == "yes":
            self.db_helper.write(sql)

    def delete_log(self):
        self.id = int(input("Enter Log ID: "))

        sql = f"delete from HealthLogger where id = {id}".format_map(
            vars(self))

        print(sql)

        delete = input("Do you wish to Delete the record (yes/no)")
        if delete == "yes":
            self.db_helper.write(sql)


    def get_all_logs(self):
        sql = "select * from HealthLogger"
        self.db_helper.read(sql)

    def get_logs_by_phone(self, phone):
        sql = "select * from HealthLogger where phone = {}".format(phone)
        self.db_helper.read(sql)

print("===============")
print("WELCOME")
print("HEALTH LOGGER APP")
print("===============")

while True:

    print("1: Insert a new Health Log")
    print("2: Update an Existing Health Log")
    print("3: Delete an Existing Health Log")
    print("4: Get all Health Logs")
    print("5: Get all Health Logs by Phone")

    option = int(input("Enter your option: "))

    if option == 1:
        print("Create a new Health Log")
        logger = HealthLogger()
        logger.save_log()

    elif option == 2:
        print("Update an Existing Health Log")
        logger = HealthLogger()
        logger.update_log()

    elif option == 3:
        print("Delete Existing Health Log")
        logger = HealthLogger()
        logger.delete_log()

    elif option == 4:
        print("Get all Health Logs")
        logger = HealthLogger()
        logger.get_all_logs()

    elif option == 5:
        print("Get all Health Logs by Phone")
        logger = HealthLogger()
        logger.get_logs_by_phone(input("Enter Phone Number: "))

    else:
        print("Invalid option")

    choice = input("Would you like to add another Health Log... (yes/no)")
    if choice == "no":
        break




