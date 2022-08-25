
# 1 1
# 2 11
# 3 111
# 4 121
# 5 1211
# 6 1221
# 7 12211
# 8 12221
# 9 12321
# 10 123211
# 11 123221
# 12 123321
# 13 1233211
# 14 1233221
# 15 1233321
# 16 1234321
# 17 12343211
# 18 12343221
# 19 12343321
# 20 12344321

from sys import stdin
rl = stdin.readline

lenList = []
maxLen = None
for _ in range(int(input())):
    a,b = map(int, rl().split())
    lenList.append(b-a)
maxLen = max(lenList)

# i = 1
# _len = 3
# ansList = [1]
# while max(ansList) < maxLen:
#     ansList.append(i + _len//2)
#     ansList.append(i + _len)
#     i += _len
#     _len += 2
# print(ansList)

i = 2
_len = 2
ansList = [1,2] 
while i < maxLen:
    i += _len
    ansList.append(i)
    i += _len
    ansList.append(i)
    _len += 1
    
print(ansList)

for l in lenList:
    if l == 1:
        print(1)
    else:
        low, high = 0, len(ansList)-1
        while low <= high:
            mid = (high + low) //2
            if ansList[mid] < l <= ansList[mid+1]:
                print(mid+2)
                break
            elif ansList[mid] >= l:
                high = mid -1
            else:
                low = mid + 1

