import logging as lg  #importing logging module into current python script / file

count=0 # for counting total weight
for i in dir(lg):
    count+=1
    print(i)
print("weight of logging module : ",count)


# OTHER WAY TO PRINT CONTENTS OF LOGGING MODULE

print(dir(lg))



