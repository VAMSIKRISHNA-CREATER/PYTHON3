def findMissingNumb(given_list):
    n = len(given_list)
    length = n + 1
    totalSum = length * (length + 1) / 2
    arraysum = 0
    for ele in given_list:
        arraysum = arraysum+ele
    missnum = totalSum-arraysum
    return int(missnum)
given_list = [1, 3, 2, 6, 5]

print("The missing number in the given list", findMissingNumb(given_list))
