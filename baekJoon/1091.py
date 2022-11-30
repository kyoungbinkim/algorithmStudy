from sys import stdin

def iter(l, s, size):
    ans = [None] * size

    for i in range(size):
        ans[s[i]] = l[i]
    return ans

def check(arr, size):
    for i in range(size):
        if arr[i]%3 != i%3:
            return False
    return True

size = int(stdin.readline())

deck = list(map(int, stdin.readline().split()))
start = deck.copy()
S = list(map(int, stdin.readline().split()))
ans = 0

while not check(deck,size):
    deck = iter(deck, S, size)
    ans += 1

    if deck == start:
        ans = -1
        break
print(ans)



