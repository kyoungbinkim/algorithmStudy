from copy import deepcopy
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def up(a, size):
    arr = deepcopy(a)
    for i in range(size):       #col
        for j in range(size):   #row
            if arr[j][i] == 0:
                for k in range(j+1, size):
                    if arr[k][i] == 0:
                        continue
                    else:
                        arr[j][i] = arr[k][i]
                        arr[k][i] = 0
                        break
                
            for k in range(j+1, size):
                if arr[k][i] == 0:
                    continue
                elif arr[k][i] == arr[j][i]:
                    arr[k][i] = 0
                    arr[j][i] = arr[j][i]*2
                break
    return arr

def down(a, size):
    arr = deepcopy(a)
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            if arr[j][i] == 0:
                for k in range(j-1,-1,-1):
                    if arr[k][i] == 0:
                        continue
                    else:
                        arr[j][i] = arr[k][i]
                        arr[k][i] = 0
                        break
                
            for k in range(j-1,-1,-1):
                if arr[k][i] == 0:
                    continue
                elif arr[k][i] == arr[j][i]:
                    arr[k][i] = 0
                    arr[j][i] = arr[j][i]*2
                break
    return arr

def left(a,size):
    arr = deepcopy(a)
    for j in range(size):       
        for i in range(size):   
            if arr[j][i] == 0:
                for k in range(i+1, size):
                    if arr[j][k] == 0:
                        continue
                    else:
                        arr[j][i] = arr[j][k]
                        arr[j][k] = 0
                        break
                
            for k in range(i+1, size):
                if arr[j][k] == 0:
                    continue
                elif arr[j][k] == arr[j][i]:
                    arr[j][k] = 0
                    arr[j][i] = arr[j][i]*2
                break
    return arr

def right(a,size):
    arr = deepcopy(a)
    for j in range(size-1, -1, -1):       
        for i in range(size-1, -1, -1):   
            if arr[j][i] == 0:
                for k in range(i-1, -1,-1):
                    if arr[j][k] == 0:
                        continue
                    else:
                        arr[j][i] = arr[j][k]
                        arr[j][k] = 0
                        break
                
            for k in range(i-1, -1,-1):
                if arr[j][k] == 0:
                    continue
                elif arr[j][k] == arr[j][i]:
                    arr[j][k] = 0
                    arr[j][i] = arr[j][i]*2
                break
    return arr

def run(arr, ind,size):
    if ind == 0:
        t = up(arr,size)
    elif ind == 1:
        t = down(arr,size)
    elif ind == 2:
        t = left(arr,size)
    else:
        t = right(arr,size)
    return t


def dfs(arr, dep, size):
    if dep == 5:
        a = list(map(max, arr))
        return max(a)
    ans = []
    for i in range(4):
        t = run(arr,i,size)
        ans.append( dfs(t, dep+1, size) )
    return max(ans)



arr = []
size = int(stdin.readline())
for _ in range(size):
    arr.append(list(map(int, stdin.readline().split())))

# for a in left(arr,size):
#     print(a)

ans = dfs(arr,0, size)
print(ans)

# 10
# 16 16 8 32 32 0 0 8 8 8
# 16 0 0 0 0 8 0 0 0 16
# 0 0 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0

# 5
# 2 2 4 8 16
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 2 2 4 8 16

# 7
# 2 2 2 2 2 2 2
# 2 0 2 2 2 2 2
# 2 0 2 2 2 2 2
# 2 0 2 2 2 2 2
# 2 2 2 0 2 2 2 
# 2 2 2 2 2 2 0
# 2 2 2 2 2 2 0

# 4
# 0 0 0 0
# 4 0 0 0
# 8 32 4 0
# 8 8 4 0

