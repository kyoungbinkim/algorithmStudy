import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a3 = a1*b2 + a2*b1
b3 = b1*b2
GCD = math.gcd(a3,b3)

print(int(a3/GCD), int(b3/GCD))

