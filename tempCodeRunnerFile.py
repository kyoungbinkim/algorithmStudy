import math

a,b = map(int, input().split())
GCD = math.gcd(a,b)
print(GCD)
print(int(a*b/GCD))