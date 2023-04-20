
# to find the most frequent element from the list
my_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']
 
most_frequent_value = max(set(my_list), key=my_list.count)
 
print("The most common element is:", most_frequent_value)
