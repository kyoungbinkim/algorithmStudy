import math

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)+1
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

a,b = map(int, input().split())
ans =0
plist = prime_list(b)

for k in plist:
    tmp = k*k

    while tmp <= b:
        if a<= tmp <= b:
            ans +=1
        tmp = tmp*k

print(ans)
