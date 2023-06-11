# Hint : Queue
N, K = map(int,input().split())


## Solution
ans = []
arr = list(range(1,N+1))
[0,1,2,3,4,5,6] : index
[1,4,5]
idx = 0
for i in range(N):
    idx += (K-1)
    if idx >= len(arr):
        idx %= len(arr)
    ans.append(arr[idx])
    arr.pop(idx)
    # ans.append(arr.pop(idx))

print("<",', '.join(ans),">", sep="")
