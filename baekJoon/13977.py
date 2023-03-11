from sys import stdin

prime = 1000000007


factorialList = [1]
for i in range(1, 4000000):
    factorialList.append((factorialList[i-1] * (i+1)) % prime)

iter = int(stdin.readline())

for _ in range(iter):
    n,k = map(int, stdin.readline().split())
    if k==0 or n==k:
        print(1)
        continue
    ans = (factorialList[n-1] * pow(factorialList[k-1], prime-2, prime) % prime)
    ans =( ans * pow(factorialList[n-k-1], prime-2, prime) ) % prime
    print(ans)