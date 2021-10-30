import time
start = time.time()
def seperator(l):
    moves=0
    i=0
    j=1
    l1=l.copy()
    while(j<len(l)):
        if(l1[i]==l1[j]):
            j+=1

        elif(l1[i]>l1[j]):
            i=j
            j+=1
            
        elif(l1[i]<l1[j]):
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
            moves+=(j-i)
            i+=1
            j+=1

    moves1=0
    i=0
    j=1
    l2=l.copy()
    while(j<len(l)):
        if(l2[i]==l2[j]):
            j+=1

        elif(l2[i]<l2[j]):
            i=j
            j+=1
            
        elif(l2[i]>l2[j]):
            temp=l2[i]
            l2[i]=l2[j]
            l2[j]=temp
            moves1+=(j-i)
            i+=1
            j+=1
            
    return (l1,moves,l2,moves1)
        
print(seperator([1,0,1,1,0,1,1]))
end=time.time()
print()
print()
print(end-start)
