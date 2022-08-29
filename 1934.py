from math import gcd
for _ in range(int(input())):
    a,b = map(int, input().split())
    g = gcd(a,b)
    print(int(a*b/g))