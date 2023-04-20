import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Reading the Employee data      
    cur.execute("select name, id, salary from Employee")  
  
    #fetching the first row from the cursor object  
    result = cur.fetchone()  
  
    #printing the result  
    print(result)  
  
except:  
    myconn.rollback()  
      
myconn.close()  
