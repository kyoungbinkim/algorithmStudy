from sys import stdin

n = int(stdin.readline())
paper = [[0 for _ in range(100)] for _ in range(100) ]

for _ in range(n):
    x, y = map(int ,stdin.readline().split())

    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            paper[i][j] = 1

ans = sum ( [sum(p) for p in paper] )
print(ans)