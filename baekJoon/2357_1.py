from sys import stdin

tree = [0] * 200000

n,m = map(int, stdin.readline().split())
treeSize,tmp = 0,n
while True:
    treeSize += tmp
    if tmp == 1:
        break
    tmp = round(tmp/2)
    print(tmp)

# 10 5 