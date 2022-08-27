from sys import stdin

col, row = map(int, stdin.readline().split())
arr=[]
for _ in range(row):
    arr.append(list(map(int, stdin.readline().split())))

for a in arr:
    print(a)