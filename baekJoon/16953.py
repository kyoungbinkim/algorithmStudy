import sys
sys.setrecursionlimit(10**9)
def search(n, target):
    if n == target:
        return 1
    elif n>target:
        return float("inf")
    
    return min(search(2*n, target), search(10*n+1, target))+1

a,b = map(int, input().split())
ans = search(a,b)
if ans == float("inf"):
    print(-1)
else:
    print(ans)