
n,m = map(int, input().split())

def myPrint(ans):
    for i in range(len(ans)-1):
        print(ans[i], end=" ")
    print(ans[len(ans)-1])

def hi(l, dep, ans):
    if len(ans) == dep:
        myPrint(ans)
        return
    if len(ans) == 0:
        for i in l:
            hi(l, dep, ans+[i])
    else:
        for i in range(ans[len(ans)-1], l[len(l)-1]+1):
            hi(l, dep, ans+[i])

hi(list(range(1, n+1)), m, [])