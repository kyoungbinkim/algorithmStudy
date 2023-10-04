from sys import setrecursionlimit
setrecursionlimit(10**9)

visit = set()
ans = [-1 for _ in range(1000001)]
ans[0] = 0

def solution(x, y, n):
    ans[x] = 0
    for i in range(x+1, y+1):
        tmp = float('inf')
        if i-n >= 1 and ans[i-n] >= 0:
            tmp = ans[i-n] + 1
        
        if i%2 == 0 and ans[i//2] >= 0:
            tmp = min(tmp, ans[i//2] + 1)
        
        if i%3 == 0 and ans[i//3] >= 0:
            tmp = min(tmp, ans[i//3] + 1)
        ans[i] = tmp if tmp != float("inf") else -1
    print(ans[y])
        
        
    return ans[y]