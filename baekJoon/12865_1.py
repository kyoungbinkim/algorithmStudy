from sys import stdin

n, th = map(int ,stdin.readline().split())

wList = [0] * (th+1)

wMap = {0:0}

for _ in range(n):
    w,v = map(int, stdin.readline().split())
    
    keys = list(wMap.keys())
    keys.sort(reverse=True)

    for weight in keys:
        if weight + w > th:
            continue
        if wMap.get(weight + w) == None:
            wMap.update({weight +w : v + wMap[weight]})
        else:
            wMap[weight+w] = v+wMap[weight] if v+wMap[weight] > wMap[weight+w] else wMap[weight+w]

    # print(wMap)

ans = -1
for k in wMap.keys():
    ans = wMap[k] if wMap[k] > ans else ans
print(ans)
    

