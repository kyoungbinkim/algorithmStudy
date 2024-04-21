from sys import stdin

n = int(stdin.readline())
ans = set()
sList = list(map(int, stdin.readline().split()))
posList = [[sList[0], 0, sList[0]*2, 0]]

for (idx, s) in enumerate(sList[1:]):
    pos = [s, 0 , 2*s, idx+1]


    for before in posList:
        if before[0] < s:
            start = before[2] + before[0] - s 
            end = before[2] + before[0] + s 
        elif before[0] > s:
            start = before[2] - before[0] + s
            end = before[2] - before[0] + 3 * s 
        else:
            start = before[2] 
            end = before[2] + s * 2 

        if end > pos[2]:
            pos = [s, start, end, idx+1]
    posList.append(pos)
posList.sort(key=lambda x: x[0], reverse=True)        

line = [False for _ in range(200010)]
for (s, start, end , idx) in posList:
    for i in range(start, end):
        if line[i] == False:
            ans.add(idx)
            line[i] = True

ans = list(ans)
ans.sort()
ans = [str(x+1) for x in ans]
print(' '.join(ans))