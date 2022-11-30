from sys import stdin

def check(n):
    if n < 0:
        return 0
    ans = 45 * (n//10) + sum(range(1,n%10+1))

    for i in range(1, len(str(n))):
        ten = 10**i
        l = n//(ten*10)
        r = n % ten
        pos = (n//ten)%10

        for j in range(10):
            ans += j * l * ten
        
        for j in range(pos):
            ans += j * ten
        
        ans += (r + 1) * pos
    return ans


for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    print(check(m) - check(n-1))
    