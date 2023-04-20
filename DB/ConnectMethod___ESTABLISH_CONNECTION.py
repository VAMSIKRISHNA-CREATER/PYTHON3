import mysql.connector as msc

# GETTING MYSQL.CONNECTOR INTO CURRENT FILE


# way 01

conn = msc.connect(
        host="localhost" , # '127.0.0.8'
        user="root",
        password="root",
        database=None,
        use_pure=None
    ) #connect() method returns MySqlConnection object.
if(conn):
    print("connection established successfuly")
else:
    print("Error...! Failed to establish connection")




#  way  02

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print("Connection Established")
except Error as e:
    print(e)




