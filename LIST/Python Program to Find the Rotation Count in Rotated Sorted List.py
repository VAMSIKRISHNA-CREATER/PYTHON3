gvn_lst = [1, 3, 5, 7, 9]
len_lst = len(gvn_lst)
minim_index = gvn_lst[0]
for itr in range(0, len_lst):
    if (minim_index > gvn_lst[itr]):
        minim_index = gvn_lst[itr]
        minim_index = itr
print("The number of rotations of a gvn_lst", gvn_lst, "=", minim_index)
