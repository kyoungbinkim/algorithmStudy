from sys import stdin

size = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
ans = [[-1]*size for _ in range(size)]

