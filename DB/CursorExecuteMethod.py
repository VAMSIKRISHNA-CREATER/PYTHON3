import mysql.connector as msc

try:
    connection = msc.connect(
            host="localhost",
            user="root",
            password="root",
        )
    curs = connection.cursor()
    curs.execute("show databases")
    for i in curs:
        print(i)
    connection.close()
except Exception as e:
    print(e)
