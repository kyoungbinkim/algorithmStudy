from sys import stdin

n = int(stdin.readline())
classMate = []
score = [0 for _ in range(n)]

ans = { }

for i in range(n):
    classMate.append(list(map(int, stdin.readline().split())))
    ans[i] = set()

for year in range(5):
    tmp = {}
    thisYear = [line[year] for line in classMate]
    for i in range(n):
        
        if tmp.get(thisYear[i]) == None:
            tmp[thisYear[i]] = set()
        tmp[thisYear[i]].add(i)
    
    for k in tmp.keys():

        for stu in tmp[k]:
            ans[stu] = ans[stu].union(tmp[k])

idx, maxLen = 0, len(ans[0])

for i in range(1, n):
    if len(ans[i]) > maxLen:
        maxLen = len(ans[i])
        idx = i

print(idx+1)