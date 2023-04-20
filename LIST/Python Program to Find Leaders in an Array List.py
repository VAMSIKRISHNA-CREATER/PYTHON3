gvnlstt = [23, 11, 1, 7, 8, 6, 3]
lstleng = len(gvnlstt)
print('The leaders of the given list', gvnlstt, 'are :')
for m in range(lstleng):
    for n in range(m+1, lstleng):
        if (gvnlstt[m] <= gvnlstt[n]):
            break
    if(n == lstleng-1):
        print(gvnlstt[m])
