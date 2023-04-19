

#  os.path.isfile("stringInput") : boolean  
#  eg :--

import os
'''file = open("krishnan.docx","w+") # file creation
a=os.path.isfile("krishnan.docx")
if(os.path.isfile("krishnan.docx")):
    print("It is file")
    print(a)'''


#  os.path.isdir("stringInput") : boolean
#  eg:-
#os.mkdir("vam")  
#if(os.path.exists("vam")):
#    print("Directory already created")


#  read([size])
#  read() is file object method , accepts 1 int type parameter (formal_argument)
#  if we pass the count then that time read() method will returns a string
#    ( length of returned string depends on input int parameter )
#  eg :

file1=open("vamsi.py","r")
#file1.write("print(\'hello world\')")
print(f"file {file1.name} created")
print("file pointer is at : ",file1.tell())
print(file1.read(10))
print("file pointer is at : ",file1.tell()) # returns integer represents the file pointer position
print(file1.read())
file1.seek(0)
print(file1.read())


file1.seek(0)	#Move file pointer to the beginning of a File
file1.seek(5)	#Move file pointer five characters ahead from the beginning of a file.
file1.seek(0, 2)	#Move file pointer to the end of a File
file1.seek(5, 0)	#Move file pointer five characters ahead from the current position.
#file1.seek(-5, 0)	#Move file pointer five characters behind from the current position.
#file1.seek(-5, 2)	#Move file pointer in the reverse direction. Move it to the
                #5th character from the end of the file

'''
    f.seek(offset, whence)
       *) How many points the pointer will move is computed from adding offset
          to a reference point; the reference point is given by the whence argument.

       *) The allowed values for the whence argument are: –
           1) A whence value of 0 means from the beginning of the file.
           2) A whence value of 1 uses the current file position
           3) A whence value of 2 uses the end of the file as the reference point.

    NOTE :  If your using seek() function in text files (those opened without a b
            in the access mode), only seeks relative to the beginning of the file are allowed.
            If you try to move the file handle from the current position you’ll
            get an io.UnsupportedOperation: can't do nonzero cur-relative seeks error.
            So open the file in binary mode if you want to move the file pointer
            ahead or behind from the current position

'''


with open(r'vamsi.py', "rb") as fp:
    # Move the file handle to the 5th character
    # from the beginning of the file
    fp.seek(3)
    # read 5 bytes and convert it to string
    print(fp.read(5).decode("utf-8"))

    # Move the fp 10 points ahead from current position
    # read 5 bytes and convert it to string
    fp.seek(10, 1)
    # again read 6 bytes
    print(fp.read(6).decode("utf-8"))


"""
    RawString literal :-
                            r'stringContent'     (or)     r"stringContent"

                IT IS USEFUL WHEN WE WANT TAKE USER IPUT AS IT IS.
                MOSTLY USED IN FILES CONCEPT ( while reading :   absolute paths  )
                BCOZ OF \ SYMBOL WE BOUND TO GET ERROR
"""




'''

Deleting file using the os module and pathlib module
Deleting files from a directory
Remove files that match a pattern (wildcard)
Delete empty directory
Delete content of a directory (all files and sub directories)

    os.remove('file_path')	          Removes the specified file.
    os.unlink('file_path')	          Removes the specified file. Useful in UNIX environment.
    pathlib.Path("file_path").unlink()	  Delete the file or symbolic link in the mentioned path
    os.rmdir('empty_dir_path')	Removes   the empty folder.
    pathlib.Path(empty_dir_path).rmdir()  Unlink and delete the empty folder.
    shutil.rmtree('dir_path')	          Delete a directory and the files contained in it.

   We can delete files or directories by using above funtions permanantly
   Here pathlib is introduced in python3.4 : not  recommended Bcoz it does not work properly
   when application running in other platform or os "

     
-------------------------------------------------------------
  *   PYTHON SUPPORTS VARIOUS METHODS FOR FILE HANDLING
  *   ABSOLUTE FILE PATH :   STARTS WITH ROOT DIRECTORY
  *   RELATIVE FILE PATH :   STARTS WITH .   ( dot )
-------------------------------------------------------------

 ---------< OS.REMOVE()  >----------
     -------------------------- 

  *     The OS module in Python provides methods to interact
        with the Operating System in Python.

  *     The remove() method in this module is used to remove/delete a file path.

  *     First, import the os module and Pass a file path to the os.remove('file_path') method
        to delete a file from a disk

        SYNATX  :   os.remove(path, *, dir_fd = None)
                        ---< path   : either absolute or relative >----
                        ---< dir_fd : name of the directory in which the given is present >----

        NOTE :  IF WE WANT TO DELETE ANY DIRECTORY OR FILE, FIRST OF ALL
                WE NEED TO ENSURE THAT THE FILE IS AVAILABLE OR NOT
                IF NOT AVAILABLE THEN DELETION OPERATION IS MEANINGLESS ONE

                FOR THAT WE MAKE USE OF 3 METHODS :


                
        ========================================
        import os
        # deletion by using relative path
        os.remove("vamsi.txt")
        # deletion by using absolute path
        os.remove(r"g:\temp\text\unimp\vamsi.txt")
        =========================================



  ----------< rmtree() >------------
      ----------------------

    *   shutil module provide rmtree() to delete a directory ( Either Empty or Non-Empty )
    *   Import the shutil module and pass the directory path to
        shutil.rmtree('path') function to delete a directory and
        all files contained in it.


Remove File Using os.unlink() method
If you are using the UNIX operating system use the unlink() method available in the OS module, which is similar to the remove() except that it is more familiar in the UNIX environment.

os.unlink(path, *, dir_fd=None)
path – A relative or absolute path for the file object generally in string format.
dir_fd – A directory representing the location of the file. The default value is none and this value is ignored in the case of an absolute path.
Let us see the code for deleting the file “profits.txt” which is in the current execution path.

import os

os.unlink('profits.txt')
Pathlib Module to Remove File
The pathlib module offers classes representing filesystem paths with semantics appropriate for different operating systems. Thus, whenever we need to work with files in multiple environments, we can use the pathlib module.

The pathlib module was added in Python 3.4. The pathlib.path.unlink() method in the pathlib module is used to remove the file in the mentioned path.


Also, it takes one extra parameter, namely missing_ok=False. If the parameter is set to True, then the pathlib module ignores the File Not Found Error. Otherwise, if the path doesn’t exist, then the FileNotFoundError will be raised.

Let us see the code for deleting the file “profits.txt” which is present in the current execution path.

Import a pathlib module
Use pathlib.Path() method to set a file path
Next, to delete a file call the unlink() method on a given file path.
import pathlib

# Setting the path for the file
file = pathlib.Path("profits.txt")
# Calling the unlink method on the path
file.unlink()
Delete all Files from a Directory
Sometimes we want to delete all files from a directory without deleting a directory. Follow the below steps to delete all files from a directory.

Get the list of files in a folder using os.listdir(path) function. It returns a list containing the names of the files and folders in the given directory.
Iterate over the list using a for loop to access each file one by one
Delete each file using the os.remove()

Example:

import os

path = r"E:\demos\files\reports\\"
for file_name in os.listdir(path):
    # construct full file path
    file = path + file_name
    if os.path.isfile(file):
        print('Deleting file:', file)
        os.remove(file)
Delete an Empty Directory (Folder) ===>  rmdir()
                                                 =====< os.rmdir() >=
                ---------------------------------
                os.rmdir(path, *, dir_fd = None)
                ---------------------------------

            path   – A relative or absolute path
            dir_fd – File directory. The default value is none, and this value is ignored in the case of an absolute path.

Note: In case if the directory is not empty then the OSError will be thrown.

import os

# Deleting an empty folder
directory = r"E:\pynative\old_logs"
os.rmdir(directory)
print("Deleted '%s' directory successfully" % directory)


Use pathlib.Path.rmdir()

The rmdir() method in the pathlib module is also used to
remove or delete an empty directory.

First set the path for the directory
Next, call the rmdir() method on that path
Let us see an example for deleting an empty directory called ‘Images’.

import pathlib

# Deleting an empty folder
empty_dir = r"E:\pynative\old_images"
path = pathlib.Path(empty_dir)
path.rmdir()
print("Deleted '%s' directory successfully" % empty_dir)

Delete a Non-Empty Directory using shutil
Sometimes we need to delete a folder and all files contained in it. Use the rmtree() method of a shutil module to delete a directory and all files from it. See delete a non-empty folder in Python.

The Python shutil module helps perform high-level operations in a file or collection of files like copying or removing content.

shutil.rmtree(path, ignore_errors=False, onerror=None)
Parameters:

path – The directory to delete. The symbolic links to a directory are not acceptable.
ignore_errors – If this flag is set to true, then the errors due to failed removals will be ignored. If set to true, the error should be handler by the function passed in the one error attribute.
Note: The rmtree() function deletes the specified folder and all its subfolders recursively.

Consider the following example for deleting the folder ‘reports’ that contains image files and pdf files.

import shutil

# Deleting an non-empty folder
dir_path = r"E:\demos\files\reports"
shutil.rmtree(dir_path, ignore_errors=True)
print("Deleted '%s' directory successfully" % dir_path)

Output

Deleted 'E:\demos\files\reports' directory successfully 
Get the proper exception message while deleting a non-empty directory

In order to get the proper exception message we can either handle it in a separate function whose name we can pass in the oneerror parameter or by catching it in the try-except block.

import shutil

# Function for Exception Handling
def handler(func, path, exc_info):
    print("We got the following exception")
    print(exc_info)

# location
dir_path = r'E:\demos\files\reports'
# removing directory
shutil.rmtree(dir_path, ignore_errors=False, onerror=handler)

Final code: To delete File or directory

import os
import shutil

def delete(path):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        # remove file
        os.remove(path)
    elif os.path.isdir(path):
        # remove directory and all its content
        shutil.rmtree(path)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path))

# file
delete(r'E:\demos\files\reports\profits.txt')
# directory
delete(r'E:\demos\files\reports')

Deleting Files Matching a Pattern
For example, you want to delete files if a name contains a specific string.

The Python glob module, part of the Python Standard Library, is used to find the files and folders whose names follow a specific pattern.

glob.glob(pathname, *, recursive=False)
The glob.glob() method returns a list of files or folders that matches the pattern specified in the pathname argument.

This function takes two arguments, namely pathname, and recursive flag ( If set to True it will search files recursively in all subfolders)

We can use the wildcard characters for the pattern matching, and the following is the list of the wildcard characters used in the pattern matching.

Asterisk (*): Matches zero or more characters
Question Mark (?) matches exactly one character
We can specify a range of alphanumeric characters inside the [].
Example: Deleting Files with Specific Extension
On certain occasions, we have to delete all the files with a particular extension.

Use glob() method to find all text files in a folder
Use for loop to iterate all files
In each iteration, delete single file.

Let us see few examples to understand how to use this to delete files that match a specific pattern.

Example

import glob
import os

# Search files with .txt extension in current directory
pattern = "*.txt"
files = glob.glob(pattern)

# deleting the files with txt extension
for file in files:
    os.remove(file)
Delete file whose name starts with specific string
import glob
import os

# Delete file whose name starts with string 'pro'
pattern = r"E:\demos\files\reports\pro*"
for item in glob.iglob(pattern, recursive=True):
    os.remove(item)
 Run
Delete file whose name contains a specific letters
We can give a range of characters as the search string by enclosing them inside the square brackets ([]).


The following example will show how to delete files whose name contains characters between a-g.

import glob
import os

# search files like abc.txt, abd.txt
pattern = r"E:\demos\files_demos\reports\[a-g]*.txt"
for item in glob.iglob(pattern, recursive=True):
    os.remove(item)
Deleting Files Matching a Pattern from all Subfolders
While the glob() function finds files inside a folder, it is possible to search for files inside the subfolders using the iglob() function which is similar to the glob() function.

The iglob() function returns iterator options with the list of files matching a pattern inside the folder and its subfolder.

We need to set the recursive flag to True when we search for the files in subdirectories. After the root folder name, we need to pass ** for searching inside the subdirectories.

import glob
import os

# Searching pattern inside folders and sub folders recursively
# search all jpg files
pattern = r"E:\demos\files\reports\**\*.jpg"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)

# Uncomment the below code check the remaining files
# print(glob.glob(r"E:\demos\files_demos\reports\**\*.*", recursive=True))

Output

Deleting: E:\demos\files\reports\profits.jpg
Deleting: E:\demos\files\reports\revenue.jpg
Conclusion
Python provides several modules for removing files and directories.

To delete Files: –

Use os.remove() and os.unlink() functions to delete a single file
Use pathlib.Path.unlink() to delete a file if you use Python version > 3.4 and application runs on different operating systems.
To delete Directories


Use os.rmdir() or pathlib.Path.rmdir() to delete an empty directory
use the shutil.rmtree() to recursively delete a directory and all files from it.
Take due care before removing files or directories because all the above functions delete files and folders permanently.







'''

import os

# remove file with absolute path
os.remove(r"E:\demos\files\sales_2.txt")







