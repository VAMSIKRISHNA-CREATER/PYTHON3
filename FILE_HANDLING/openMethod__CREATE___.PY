# file handling

#  open(filename,mode)
'''
     *   open(filename,mode) , IT IS A BUILT IN METHOD IN PYTHON
     *   IT ACCEPTS TWO PARAMETERS ONE IS NAME OF THE FILE SECOND IS MODE
         MODE IS USEFUL PARAMETER WHY BCOZ IT IDICATES  IN WHICH WAY WE WANT TO OPEN
         A FILE.

         SYNTAX :        FILE = open(NAME_OF_THE_YOUR_FILE,FILE_OPENING_MODE)
         
         MODE --> ( r ==>  for reading an existing file
                    w ==>  TO PERFOM WRITE OPERATION ON EXISTING FILE
                          IF ALREADY DATA IS THERE , AT THAT TIME DATA WILL BE OVERRIDEN
                          **** IF THE FILE DOES NOT EXIST ON THAT TIME IT WILL CREATE ONE
                          NEW FILE WITH GIVEN FILE NAME .
                    a ==> IT IS USED TO INDICATE WE ARE GOING TO OPEN FILE IN APPEND MODE
                          HERE IT WON'T OVERRIDE  EXISTING DATA.
                   r+ ==> READ & WRITE OPERATIONS.
                          PREVIOUS DATA WILL BE OVERRIDEN
                   w+ ==> WRITE & READ OPERATIONS.
                          OVERRIDE EXISTING DATA.
                   a+ ==> APPEND & READ MODE.
                          HERE IT WON'T OVERRIDE THE EXISTING DATA.

                          )
'''
try:
    file = open("vamsi.txt","r+")
    print("one file created with vamsi.txt name")
except Exception as prob:
    print("Here the problem is : \n",prob)









