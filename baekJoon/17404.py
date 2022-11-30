from sys import stdin
rl = stdin.readline
 
houses = []
lastInd = []
for _ in range(int(rl())):
    houses.append(list(map(int, rl().split())))
    lastInd.append([0]*3)

for ind in range(len(houses)-2, -1, -1):
    for i in range(3):
        houses[ind][i] += min(houses[ind+1][(i+1)%3], houses[ind+1][(i+2)%3])
print(min(houses[0]))