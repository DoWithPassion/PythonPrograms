'''
#Given a list of strings find the minimum
# possible rotations on strings to make all strings
# equal else return -1
'''
def minrotations(arr):
    if not arr: return -1
    n=len(arr[0])
    cnt = {(arr[0][i:]+arr[0][:i]):i for i in range(n)}
    for s in arr[1:]:
        if(len(s)!=n): return -1
        for i in range(n):
            cur = s[i:] + s[:i]
            if cur not in cnt:
                return -1
            cnt[cur]+=i
    return cnt[min(cnt,key = lambda x: cnt[x])]
arr = ["11234", "34112", "41123", "11234"]
print(minrotations(arr))
