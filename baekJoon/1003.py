def fiboHit(n):
    if n == 0:
        return [1,0]
    elif n== 1:
        return [0,1]
    b1 = [1,0]
    b2 = [0,1]
    for i in range(2, n+1):
        ret = [b1[0]+b2[0], b1[1]+b2[1]]
        b1 = b2
        b2 = ret
    return ret
    
for _ in range(int(input())):
    tmp = int(input())
    ans = fiboHit(tmp)
    print(ans[0], ans[1])

