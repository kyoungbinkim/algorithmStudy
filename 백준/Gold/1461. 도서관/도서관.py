from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())

books = list(map(int, stdin.readline().split()))
books.sort()

def minus(books):
    ans = 0
    while len(books) and books[0] < 0:
        ans += abs(books.popleft()) * 2
        for _ in range(m-1):
            if len(books) and books[0] < 0:
                books.popleft()
            else:
                break
    return ans

def plus(books):
    ans = 0
    while len(books) and books[-1] > 0:
        ans += abs(books.pop()) * 2

        for _ in range(m-1):
            if len(books) and books[-1]> 0:
                books.pop()
            else:
                break
    return ans

ans = -1 * max(abs(books[0]), abs(books[-1]))
books = deque(books)

ans += minus(books)
ans += plus(books)
print(ans)

