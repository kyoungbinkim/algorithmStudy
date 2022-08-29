from sys import stdin
import math
l,r,k = int(stdin.readline()), int(stdin.readline()), int(stdin.readline())

# l      <= k * (x + x+(k-1)d) / 2  <= r
# 2l / k <=       2x + (k-1)d       <= 2r / k

left, right = math.ceil(2 * l / k), math.floor(2 * r / k)
# print(2 * l / k, 2 * r / k)
mright, mleft = max([right, 2+k-1]) , max([left, 2+k-1])
# print(left, right, k+1)

if k % 2 == 0:
    ans = abs(mright - mleft) + 1
    
    if k == 4 and (mleft<= 6 and 6 <= mright):
        ans -=1
    if right < k+1:
        ans = 0
    
else:
    ans = (mright - mleft)//2 +1
    if mright%2 == 1 and mleft%2 ==1:
        ans -= 1
    if right < k+1:
        ans = 0
print(ans)


# k : 2 3 4 5
# k-1 1 2 3 4