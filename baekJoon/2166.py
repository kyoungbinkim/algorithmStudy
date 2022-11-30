from sys import stdin

size = int(stdin.readline())
plist = []
for _ in range(size):
    plist.append(list(map(int, stdin.readline().split())))
ans = 0

for i in range(size-1):
    ans += ((plist[i][0]+plist[i+1][0])*(plist[i][1]-plist[i+1][1]))
ans += ((plist[size-1][0]+plist[0][0])*(plist[size-1][1]-plist[0][1]))
print(round(abs(ans/2),2))