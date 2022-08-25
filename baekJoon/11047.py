from sys import stdin
rl = stdin.readline

num, price = map(int, rl().split())
coinArr = []
for _ in range(num):
    coinArr.append(int(rl()))

ans = 0
for coin in coinArr[::-1]:
    ans += price // coin
    price = price % coin
    if price == 0:
        break
print(ans)
