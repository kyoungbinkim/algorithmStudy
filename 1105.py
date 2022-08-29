from sys import stdin

l,r = map(str, stdin.readline().split())
l = l.zfill(len(r))
f = True
ans = 0
for i in range(len(r)):
    if r[i] == l[i]:
        if r[i] == '8':
            ans +=1
        continue

    if r[i] != '8' or l[i] !='8':
        print(ans)
        f = False
        break
if f:
    print(ans)
