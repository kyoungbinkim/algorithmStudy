from sys import stdin

for _ in range(int(stdin.readline())):
    vecNum = int(stdin.readline())
    vecList = []
    for _ in range(vecNum):
        vecList.append(list(map(int, stdin.readline().split())))
    