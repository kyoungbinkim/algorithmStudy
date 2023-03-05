from sys import stdin

ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
h , w = map(int, stdin.readline().split())
m = [list(map(int, stdin.readline().split())) for _ in range(h)]    

que = [[0,0]]
ansDown = [0] * h

while len(que) > 0:
    cor = que.pop(0)
    # print(que)
    # print(cor, [h,w], cor==[h-1,w-1])
    if sum(cor) == h-1:
        ansDown[cor[0]] += 1
        continue

    cur = m[cor[0]][cor[1]]
    for i in range(4):
        x,y = cor[0]+dx[i], cor[1]+dy[i]
        if x<0 or x>=h or y<0 or y >= w:
            continue
        if cur > m[x][y]:
            que.append([x,y])

ansUp = [0] * h
que = [[h-1, w-1]]
while len(que) > 0:
    cor = que.pop(0)
    # print(que)
    # print(cor, [h,w], cor==[h-1,w-1])
    if sum(cor) == h-1:
        ansUp[cor[0]] += 1
        continue

    cur = m[cor[0]][cor[1]]
    for i in range(4):
        x,y = cor[0]+dx[i], cor[1]+dy[i]
        if x<0 or x>=h or y<0 or y >= w:
            continue
        if cur < m[x][y]:
            que.append([x,y])

# print(ansDown, ansUp)
for i in range(h):
    ans += ansDown[i] * ansUp[i]
print(ans)
