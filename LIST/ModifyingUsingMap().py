# using map() function to modify the text
def squaring(n):
    return n**2
 
# driver code
if __name__ == "__main__":
    my_list = [5, 2, 90, 24, 10, 2, 95, 36]
 
    my_squared_list = list(map(squaring, my_list))
    print(my_squared_list)
