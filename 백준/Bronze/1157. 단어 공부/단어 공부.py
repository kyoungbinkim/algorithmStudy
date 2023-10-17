s=input().upper()
cnt = [0 for _ in range(26)]

for c in s:
    cnt[ord(c) - ord('A')] += 1

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(chr(cnt.index(max(cnt)) + ord('A')))