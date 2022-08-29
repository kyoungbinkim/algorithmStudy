from sys import stdin
import math
x,y,d,t = map(int, stdin.readline().split())
dist = math.sqrt(x**2 + y**2)

if d <= t:
    ans = dist
else:
    q = dist // d
    r = dist % d
    if q== 0:
        ans = min([t + abs(r  - d), dist, 2*t])
    else:
        ans = min([(q+ 1)* t,  q * t + r, dist])
print(ans)

# 0 + 초과
# dist//d 1개이상 -> 그 값 
# print("distance : ", dist)