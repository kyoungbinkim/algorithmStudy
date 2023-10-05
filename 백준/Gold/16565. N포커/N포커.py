N = int(input())
prime = 10007

def comb(n,m):
    if m == 0:
        return 1
    k = m if m < n-m else n-m

    ans = 1
    for i in range(k):
        ans = (ans * (n-i)) % prime
        ans = (ans * pow(i+1, prime-2, prime)) % prime
    return ans

# c = -2b + (N - 3a)
def calcL1(b, n, a):
    return -2 * b + n - 3 * a

# c <= -b + 13 -a
def calcL2(b, n, a):
    return -1 * b + 13 - a

def calcLine(n,a):
    ans = []

    for b in range(0,14):
        th = calcL2(b, n, a)
        c  = calcL1(b, n, a)

        if 0 <= c <= th:
            ans.append((a,b,c))
    # print(ans)
    return ans

def calcABC(abc):
    
    total, ans = 13, 1

    for alphabet in abc:
        ans *= comb(total, alphabet)
        ans = ans % prime
        total -= alphabet

    ans *= 4 ** (abc[0] + abc[2])
    ans = ans % prime

    for _ in range(abc[1]):
        ans *= 6
        ans %= prime

    return ans

def makeABC(n):
    ans = comb(52,n)
    for a in range(n//3+1):
        abcList = calcLine(n, a)
        for abc in abcList:
            ans -= calcABC(abc)
            ans += prime
            ans = ans % prime
    return ans

print(makeABC(N))