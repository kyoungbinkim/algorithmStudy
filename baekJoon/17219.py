from sys import stdin

n,m = map(int, stdin.readline().split())
D = {}
for _ in range(n):
    tmp = stdin.readline().split()
    D.update({tmp[0]: tmp[1]})

for _ in range(m):
    print(D[stdin.readline().replace('\n','')])