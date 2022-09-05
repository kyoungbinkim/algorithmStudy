from sys import stdin
import sys

sys.setrecursionlimit(10**9)

def Search(n,k, bef):
    if n == k:
        return 1
    elif n > k or n <= 0:
        return float("inf")
    return min([Search(n+1,k),Search(n-1,k),Search(n*2,k)])+1

n,k = map(int, stdin.readline().split())
print(Search(n,k))