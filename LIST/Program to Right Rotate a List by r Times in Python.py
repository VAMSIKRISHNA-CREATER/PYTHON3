def rightRotateByOne(given_list):
    lastval = given_list[-1]
    for i in reversed(range(len(given_list) - 1)):
        given_list[i+1] = given_list[i]
    given_list[0] = lastval
def rightRotateList(given_list, positions):
    for numb in range(positions):
        rightRotateByOne(given_list)
given_list = [3, 9, 1, 2, 4, 5, 11, 23]
print('The list before rotating r times = ', given_list)
positions = 6
rightRotateList(given_list, positions)
print('The list after  rotating r times : ', given_list)
