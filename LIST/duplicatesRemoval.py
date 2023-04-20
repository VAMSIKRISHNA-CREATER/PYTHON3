# removing duplicates from a list using dictionaries
 
my_list_1 = [5, 2, 90, 24, 10, 2, 90, 34]
my_list_2 = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']
 
# removing duplicates from list 1
my_list_1 = list(dict.fromkeys(my_list_1))
print(my_list_1)
 
# removing duplicates from list 2
my_list_2 = list(dict.fromkeys(my_list_2))
print(my_list_2)
