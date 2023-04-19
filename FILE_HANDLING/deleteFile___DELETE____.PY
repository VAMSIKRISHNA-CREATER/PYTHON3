'''
       Here the important concept is
       If I want to remove or delete a fie we need check once wether that file is existing or not
       If there, We can delete that file otherwise we can not delete that file from directory
       For deleting file or directory  we should make use of 3 techniques
          (1)By using os module
          (2)By using pathlib module
'''
import os,pathlib,shutil
 
#WAY-01  USING os MODULE

file = open("vamsi.txt",'r')
print(f"one file created with a name : {file.name}\n")
#file.write("vamsikrishna  pathallapalli")
print(file.read())
file.close()

# deleting vamsi.txt file
#os.remove("vamsi.txt")                        ***** deleting vmasi.txt *****
#if(not os.path.exists("vamsi.txt")):
#    print("File Deletion Done")


#WAY-02 USING .unlink() method
#os.unlik()
#pathlib.unlink()

#os.unlink("vamsi.txt")
#if(not os.path.exists("vamsi.txt")):
#    print("File Deletion Done")

#path = pathlib.Path("vamsi.txt")

#path.unlink()
#if(not os.path.exists("vamsi.txt")):
#    print("File Deletion Done")
















