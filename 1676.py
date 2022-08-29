num = int(input())
ans = 0
for i in range(0, num+1, 5):
    if i == 0:
        continue
    while i % 5 == 0:
        ans += 1
        i = i//5
print(ans)
