import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Deleting the employee details whose id is 110  
    cur.execute("delete from Employee where id = 110")  
    myconn.commit()  
except:  
      
    myconn.rollback()  
  
myconn.close()  
