w=[int(x) for x in input().split()]
p=[int(x) for x in input().split()]
n=len(w)
m=50
u=m
pw=[p[i]/w[i] for i in range(n)]
l=list(zip(w,p,pw))
l.sort(reverse=True, key=lambda x:x[2])

max_profit=0
x=[0 for i in range(n)]
for i in range(0,n):
    if(l[i][0]>u):
        break
    x[i]=1
    u=u-l[i][0]
if(i<n):
    x[i]=u/w[i]
print(x)

for i in range(n):
    print(l[i][1])
    max_profit+=l[i][1]*x[i]
print(max_profit)
