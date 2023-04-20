
# filtering with the help of list comprehension
my_list = [5, 2, 90, 24, 10, 2, 95, 36]
 
# an elegant way to sort the list
my_list = [item for item in my_list if item > 20]
print(my_list)
