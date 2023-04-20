import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
#creating the cursor object  
cur = myconn.cursor()  
try:  
    #Reading the Employee data      
    cur.execute("select name, id, salary from Employee")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
    #printing the result  
    for x in result:  
        print(x);  
except:  
    myconn.rollback()  
myconn.close()  
