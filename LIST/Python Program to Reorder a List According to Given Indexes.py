gvn_lst = [9, 8, 2, 1]
gvn_indxlst = [1, 3, 0, 2]
len_gvn_lst = len(gvn_lst)
tempry = [0] * len_gvn_lst
for itror in range(0, len_gvn_lst):
    tempry[gvn_indxlst[itror]] = gvn_lst[itror]
for itror in range(0, len_gvn_lst):
    gvn_lst[itror] = tempry[itror]
    gvn_indxlst[itror] = itror
print("The given list after reordering according to the given indexes list :")
for itror in range(0, len_gvn_lst):
    print(gvn_lst[itror], end=" ")
print()
print("The Index list after reordering:")
for itror in range(0, len_gvn_lst):
    print(gvn_indxlst[itror], end=" ")
