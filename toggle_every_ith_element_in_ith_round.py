##There are n bulbs that are Initially off, You first turn on all the bulbs,
##Then you turn of every second bulb. On the third tIme, You toggle everything
##but Tum of its on and turn on its off). For the nth round you only toggle the
##last bub. Find how many bulb or on after n rounds
##

##n = int(input())
##l = [1 for i in range(n)]
##
##def toggle(j):
##    j=j-1
##    if l[j]==1:
##        l[j]=0
##    else:
##        l[j]=1
##
##for i in range(2,n+1):
##    for j in range(i,n+1):
##        if j%i == 0:
##            toggle(j)
##        
##print(sum(l))

import math
def question(n):
    return(int(math.sqrt(n)))

