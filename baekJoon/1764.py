from sys import stdin

n,m = map(int, stdin.readline().split())
A,B = set([]), set([])
for _ in range(n):
    A.add(stdin.readline().replace('\n',''))
for _ in range(m):
    B.add(stdin.readline().replace('\n',''))

C = list(A.intersection(B))
C.sort()
print(len(C))
for tmp in C:
    print(tmp)