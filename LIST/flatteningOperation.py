# to flatten a list_of_lists by using list comprehension
list_of_lists = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]
 
# using list comprehension
my_list = [item for List in list_of_lists for item in List]
print(my_list)
