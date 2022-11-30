from sys import stdin
def factorization(x):
    d = 2
    ans = []
    while d <= x:
        if x % d == 0:
            ans.append(d)
            x = x / d
        else:
            d = d + 1
    return ans

def BFS(n):
    que = ["1"]
    
    while True:
        tmp = que[0]
        del que[0]

        que.append(tmp+"1")
        que.append(tmp+"0")

        if int(tmp)% n ==0:
            return tmp


for i in range(1, 201):
    ans = 1
    fac = factorization(i)
    for n in fac:
        ans = ans * int(BFS(n))
    print(ans)

def BFS(nList, ansList):
    que = ["1"]
    
    flag = True
    while flag:
        tmp = que[0]
        del que[0]

        que.append(tmp+"0")
        que.append(tmp+"1")
        for i in range(len(nList)):
            if ansList[i] != 0:
                continue
            if int(tmp) % int(nList[i])  == 0:
                ansList[i] = int(tmp)
        flag = False
        for i in range(len(ansList)):
            if ansList[i] == 0:
                flag = True
                break
        

nL = []
while True:
    tmp = stdin.readline().replace("\n",'')
    if int(tmp) == 0:
        break
    nL.append(tmp)
aL = [0] * len(nL)
BFS(nL, aL)
for a in aL:
    print(a)    


