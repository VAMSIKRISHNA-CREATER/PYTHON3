#  fileHandling
#  SYNTAX :   read([countOfChars]) method
#  if pass 1 for read() method it will results only one char from the file.
try:
    file = open("temp.txt","r+")  #if i use w or w+  then , the existing data will be arised and remains as empty file
    #file.write("WELCOME TO jspider")
    print(file.read()) # if mode is w or w+ then existing data is arised and empty content will be printed
except Exception as e:
    print("Here the problem is : \n",e)
