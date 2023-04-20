ef my_filter(n):
    if n > 20:
        return n
 
       
# driver code
if __name__ == "__main__":
    my_list = [5, 2, 90, 24, 10, 2, 95, 36]
    my_filtered_list = list(filter(my_filter, my_list))
    print(my_filtered_list)
n
