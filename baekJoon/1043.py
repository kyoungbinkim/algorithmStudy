from sys import stdin
from itertools import combinations

people, party = map(int, stdin.readline().split())
know = list(map(int, stdin.readline().split()))
if know[0] > 0:
    knowSet = set(know[1:])
else:
    knowSet = set()
arr, ans = [], 0
partylist = []
for _ in range(people):
    arr.append([0]*people)

for _ in range(party):
    tmp = list(map(int, stdin.readline().split()))
    partylist.append(tmp[1:].copy())
    if tmp[0] > 1:
        for ind in combinations(tmp[1:], 2):
            x,y = ind
            arr[x-1][y-1] = 1
            arr[y-1][x-1] = 1


def DFS(arr, ind, visit, known):
    if ind+1 in known:
        return False
    visit.add(ind)
    flag = True
    for i in range(len(arr)):
        if i not in visit and arr[ind][i] == 1:
            if i+1 in known:
                return False
            flag = flag and DFS(arr, i, visit, known)
    return flag

if know[0] == 0:
    print(party)
else:
    for p in partylist:
        if DFS(arr, p[0]-1, set(), knowSet):
            ans += 1
    print(ans)