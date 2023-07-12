from sys import stdin

n = int(stdin.readline())
vArr = [[] for _ in range(n)]
visit = [False for _ in range(n)]

for _ in range(n-1):
    x,y = map(int , stdin.readline().split())

    vArr[x-1].append(y-1)
    vArr[y-1].append(x-1)

def sns(e):
    for i in e:
        visit[i] = True
    next = []

    for i in e:
        for j in vArr[i]:
            if not visit[j]:
                next.append(j)
    return next

e = [8]

while len(e) > 0:
    print(e)
    e = sns(e)
    




