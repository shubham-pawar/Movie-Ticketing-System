import mysql.connector


#Following function will create a mysql connection.
def mysql_connection():
    #Get your DB connection from "DataBase Info" Tab
    HOST = 'localhost'
    USERNAME = 'b2e154bc'
    PASSWORD = 'Cab#22se'
    DATABASE = 'b2e154bc'

    mydb = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    
    return mydb