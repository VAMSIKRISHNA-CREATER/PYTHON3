def checkPair(givenlist, value):
    length = len(givenlist)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if givenlist[i] + givenlist[j] == value:
                return True
    return False
given_list = [5, 9, 2, 8, 7, 6]
value = 10
if(checkPair(given_list, value)):
    print("Pair with given sum of elements is found")
else:
    print("Pair with given sum of elements is not found")
