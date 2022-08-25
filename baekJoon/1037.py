from sys import stdin
numSize = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))
print(int(max(numList)*min(numList)))