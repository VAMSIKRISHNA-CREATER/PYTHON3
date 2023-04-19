import os
def createFile(filename):
    try:
        file = open(filename,'w')
        print(f"File Creation Done ---< {filename} >---")
    except Exception as e:
        print(f"Error while creating {filename} \nReason :  -------<{e}>--------")
def deleteFile(filename):
    try:
        print(f"Deletion of ---<{filename}>--- is done")
        os.delete(filename)
    except Exception as e:
        print(f"Error while Deleting {filename} \nReason :  -------<{e}>--------")
def renameFile(oldFile,newFile):
    try:
        os.rename(oldFile,newFile)
        print(f"---<{oldFile}>--- name renamed to ---<{newFile}>---")
    except Exception as e:
        print(f"Error while Renaming {filename} \nReason :  -------<{e}>--------")
def addText(filename,text):
    try:
        with open(filename,'a+') as file:
            file.write(text)
        print(f"Content is Appended to existing file ---<{filename}>---")
    except Exception as e:
        print("Error while appending content to  {filename} \nReason :  -------<{e}>--------")

def displayFile(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
        print("---< EOF >---")
    except Exception as e:
        print("Error while displaying content of {filename} \nReason :  -------<{e}>--------")

if(__name__=="__main__"):
    print("createFile\tdeleteFile\trenameFile\naddText\tdisplayText")
    createFile("Resume.txt")
    addText("Resume.txt","My name is Meghana sir....\nI\'m student of presass sir\nI'm from Bendapudi sir")
    displayFile("Resume.txt")








        
