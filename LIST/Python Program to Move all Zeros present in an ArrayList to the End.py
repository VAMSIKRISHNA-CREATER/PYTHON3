
emptylist = []
given_list = [7, 2, 0, 34, 56, 12, 0, 5, 6, 8, 0, 0, 9, 0, 1, 2, 4, 5]
print("the list before modification :")
print(given_list)
zeroCount = 0
for eleme in given_list:
    if(eleme != 0):
        emptylist.append(eleme)
    else:
        zeroCount = zeroCount+1
for i in range(zeroCount):
    emptylist.append(0)
print("the list after modification :")
print(emptylist)
