'''

      *  MySQL Connector/Python provides MySQLCursor class,
         which instantiates objects that can execute MySQL queries in Python.

      *  An instance of the MySQLCursor class is also called a cursor.

      *  cursor objects make use of a MySQLConnection object to interact
         with your MySQL server. To create a cursor, use the .cursor()
         method of your connection variable.

                cursor = connection.cursor()

      *  A query that needs to be executed is sent to cursor.execute() in string format.

      
         
'''
# way 01

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        with connection.cursor() as cursor:
            print("cursor object : ",cursor)
except Error as e:
    print(e)
