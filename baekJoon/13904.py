from sys import stdin

ans = 0
arr = [[] for _ in range(1001)]

N = int(stdin.readline())

def findVal(arr):
    val = max(arr)
    ind = arr.index(val)
    del arr[ind]
    return val

for _ in range(N):
    d,w = map(int ,stdin.readline().split())
    arr[d].append(w)

# print(arr)

for i in range(1000,0,-1):
    # print(arr[i])
    if len(arr[i]) == 0:
        continue
    
    ans += findVal(arr[i])
    arr[i-1] = arr[i-1] + arr[i]
print(ans)