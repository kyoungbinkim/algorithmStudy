from sys import stdin
from itertools import combinations

def myDist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def houses2chic(h, c):
    Min = float("inf")
    for p in c:
        d = myDist(p, h)
        if d < Min:
            Min = d
    return Min

def calc(h, c):
    ans = []
    for p in h:
        ans.append(houses2chic(p, c))
    return sum(ans)

n,m = map(int, stdin.readline().split())
house, chicken = [], []

for i in range(n):
    tmp = stdin.readline().replace('\n','').replace(" ","")
    for j in range(n):
        if tmp[j] == "1":
            house.append([i,j])
        elif tmp[j] == "2":
            chicken.append([i,j])

ans = float("inf")
chicken_m = list(combinations(chicken,m))
for c in chicken_m:
    tmp = calc(house, list(c))
    if tmp < ans:
        ans = tmp
print(ans)