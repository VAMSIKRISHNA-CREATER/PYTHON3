def leftRotateByOne(given_list):
    firstval = given_list[0]
    for i in range(len(given_list) - 1):
        given_list[i] = given_list[i + 1]
    given_list[-1] = firstval
def leftRotateList(given_list, positions):
    for numb in range(positions):
        leftRotateByOne(given_list)


given_list = [9, 1, 3, 10, 47, 19, 43]
print('The list before rotating r times = ', given_list)
positions = 4
leftRotateList(given_list, positions)
print('The list after rotating r times : ', given_list)
print(given_list)
