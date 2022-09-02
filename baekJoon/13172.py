from sys import stdin

n,s = 1,0
p = 1000000007
num = int(stdin.readline())
for _ in range(num):
    n1,s1 = map(int, stdin.readline().split())

    n , s= n1*n %p , (s*n1+s1*n)%p
print(pow(n,p-2, p) * s % p)