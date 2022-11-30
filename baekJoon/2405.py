from sys import stdin

nlist, size = [], int(stdin.readline())
for _ in range(size):
    nlist.append(int(stdin.readline()))
nlist.sort()
# print(nlist)

ans = abs(nlist[0] + nlist[size-1] -2*nlist[1])
minVal = nlist[0]
maxVal = nlist[size-1]
for i in range(1,size-1):
    tmp = abs(nlist[i+1] - 2 * nlist[i] + minVal)
    if tmp > ans:
        ans = tmp

for i in range(size-1):
    tmp = abs(nlist[i] - nlist[i+1]*2 + maxVal)
    if tmp > ans:
        ans = tmp
print(ans)




# 3b - (a + b + c)
# 2b - a - c
# a+c - 2b