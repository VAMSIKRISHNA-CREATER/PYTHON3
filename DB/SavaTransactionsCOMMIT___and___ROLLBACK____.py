import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google",database = "PythonDB")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    cur.execute("delete from Employee where Dept_id = 201")  
    myconn.commit()  
    print("Deleted !")  
except:  
    print("Can't delete !")  
    myconn.rollback()  
  
myconn.close()  
