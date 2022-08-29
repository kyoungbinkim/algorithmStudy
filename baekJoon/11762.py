import math
n = int(input())
ans = 0

for i in range(n//2+1):
    num2 = i
    num1 = n-2*i
    ans += math.comb(num1+num2, num1) % 10007
    ans = ans % 10007
print(ans)