from itertools import combinations
def p(arr,m):
    for i in range(m-1):
        print(arr[i], end=" ")
    print(arr[m-1])
n,m = map(int , input().split())
a = combinations(list(range(1,n+1)), m)
for i in a:
    p(i,m)