
c = {'.':0, 'X':1}
n,m = map(int, input().split())

row = [1 for _ in range(n)]
col = [1 for _ in range(m)]

b = []
for i in range(n):
    tmp = [c[s] for s in input()]
    if sum(tmp):
        row[i] = 0
    for j in range(m):
        if tmp[j]:
            col[j] = 0
print(max(sum(row), sum(col)))