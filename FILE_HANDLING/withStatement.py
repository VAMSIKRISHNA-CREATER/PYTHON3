#  file handling

#  with statement
'''
    with statement allows a user to perform various file operation in one place.
    The syntax is short and simple to use. Readability will increased when i use with statement
    So, we can handle problems( exception ) easily

    syntax  :    with open(FileName,mode) as userIdentifier:
                     //Operations
                     userIdentifier.close() --> default statement
                 
'''
try:
    with open("temp.txt","r") as file:
        print(file.read())
except Exception as e:
    print(e)
    file.close() # default statement
print("with statement closed")
#print(file.read())     result in Exception related to  " OPERATIOINS ON CLOSED FILE
"
print("file closed")
