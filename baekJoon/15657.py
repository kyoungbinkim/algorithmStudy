
def myPrint(ans):
    for i in range(len(ans)-1):
        print(ans[i], end=" ")
    print(ans[len(ans)-1])

def hi(l, dep, ans):
    if len(ans) == dep:
        myPrint(ans)
        return
    # print(ans, l)
    for i in l:
        hi(l, dep, ans+[i])
        l = list(set(l).difference(set([i])))
        l.sort()

n,m = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.sort()

hi(tmp, m, [])
