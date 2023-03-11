from sys import stdin,  setrecursionlimit

setrecursionlimit(10 ** 6)

rgbDict= {"R":1, "G":2, "B":3}
size = int(stdin.readline())

rgb_arr = []
rb_arr = []
for _ in range(size):
    tmp = stdin.readline().replace('\n', '')
    rgb_arr.append([x for x in  tmp])
    rb_arr.append([x if x != 'G' else 'R' for x in tmp])

# print(rgb_arr)
# print(rb_arr)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def DFS(arr, c, pos):
    arr[pos[0]][pos[1]] = '0'
    for i in range(4):
        x,y = pos[0] + dx[i], pos[1] + dy[i]

        if x<0 or x>= size or y<0 or y>= size:
            continue
        if arr[x][y] != c:
            continue
        DFS(arr, c, [x,y])

rgb_ans = 0
rb_ans = 0

for i in range(size):
    for j in range(size):
        if rgb_arr[i][j] != '0':
            DFS(rgb_arr, rgb_arr[i][j], [i,j] )
            rgb_ans += 1
        if rb_arr[i][j] != '0':
            DFS(rb_arr, rb_arr[i][j], [i,j] )
            rb_ans += 1

print(rgb_ans, rb_ans)