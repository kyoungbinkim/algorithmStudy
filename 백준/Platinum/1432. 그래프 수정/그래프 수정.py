from sys import stdin

n = int(stdin.readline())
deg = [0 for _ in range(n)]
p  = [[] for _ in range(n)]

for i in range(n):
    for j, tmp in enumerate(stdin.readline().removesuffix('\n')):
        if tmp == '1':
            p[j].append(i)
            deg[i] += 1

ans = [None for _ in range(n)]

cnt = n
for _ in range(n):
    for i in range(n-1, -1, -1):
        if ans[i] == None and deg[i] == 0:
            ans[i] = cnt
            cnt -= 1

            for pi in p[i]:
                deg[pi] -= 1
            break

if None in ans:
    print(-1)
else:
    for a in ans:
        print(a, end=' ')
    print()
