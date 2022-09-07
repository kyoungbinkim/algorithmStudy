from sys import stdin

arr = []
n,m = map(int, stdin.readline().split())

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

def Go(a,b,c, n,m):
    ans = ""
    for i in range(n-1):
        if i%2 == 0:
            ans += (a*(m-1) + c)
        else:
            ans += (b*(m-1) + c)
    ans += a * (m-1)
    return ans

def Go2(n,m, a):
    ans = ""
    if a[1] == 0:
        skipInd = a[0]
        f = True # r
        for i in range(n-1):
            if skipInd == i:
                ans += "D"
                continue

            if f:
                ans += ("R"*(m-1) + "D")
            else:
                ans += ("L"*(m-1) + "D") 
            f = not f
        if n-1 != skipInd:
            if f:
                ans += "R"*(m-1)
            else:
                ans += "L"*(m-1)
    else:
        skipInd = a[1]
        f = True
        for i in range(m-1):
            if skipInd == i:
                ans += "R"
                continue

            if f:
                ans += ("D"*(n-1) + "R")
            else:
                ans += ("U"*(n-1) + "R") 
            f = not f
        if m-1 != skipInd:
            if f:
                ans += "D"*(n-1)
            else:
                ans += "U"*(n-1)
    return ans

def selcect(arr, n,m):
    ans = None
    minVal = float("inf")
    for i in range(n):
        if i%2 == 0:
            # print("!!",arr[i][1:])
            v = sum(arr[i][1:])
            
            if v<minVal:
                ans = [i,0]
                minVal = v
        else:
            # print("!",arr[i][:m-1])
            v= sum(arr[i][:m-1])
            if v<minVal:
                ans = [i,0]
                minVal = v
    # print(ans, minVal)
    tmp = [0] * m
    for i in range(n):
        for j in range(m):
            if i==0 and j%2==0:
                continue
            if i == n-1 and j%2 ==1:
                continue
            tmp[j]+= arr[i][j]
    # print(tmp)
    minV = min(tmp)
    if minV < minVal:
        ans = [0,tmp.index(minV)]
    # print(ans)
    return ans

ans = ""
if n%2 == 1:
    ans = Go("R", "L","D",n, m)
elif m%2 == 1:
    ans = Go("D","U","R", m, n)
else:
    a = selcect(arr, n,m)
    ans = Go2(n,m, a)
print(ans)

# 짝 -> 오른  짝 아래
# 홀 -> 왼   홀 위
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# 4 6
# 9 9 9 9 1 1
# 8 8 1 2 3 4
# 9 8 7 6 4 1
# 1 1 2 2 1 1

9 9 9 9
1 9 9 9
9 9 9 9
9 9 9 9

9 9 9 9 
9 1 9 9
9 9 9 9
9 9 9 9



0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0