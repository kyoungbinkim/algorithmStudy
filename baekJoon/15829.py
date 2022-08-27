size= int(input())
string = input()

ans = 0
sq = 1
for i in range(size):
    ans += (ord(string[i]) - ord('a') + 1) * sq
    sq = (sq * 31) % 1234567891
    ans = ans % 1234567891
print(ans)