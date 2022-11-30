from sys import stdin

height, wid = map(int, stdin.readline().split())
arr = [list(stdin.readline().replace('\n','').strip()) for _ in range(height)]
move = [[0,1], [1,0], [0,-1], [-1,0]]
def DFS(arr, y,x, s, tar):
    s[ord(arr[y][x]) - 65] = 1
    ans = []
    for dx, dy in move:
        rx,ry = x+dx, y+dy

        if 0<= ry < height and  0<= rx < wid:           
            if s[ord(arr[ry][rx]) - 65]== 0:
                tmp = DFS(arr, ry, rx, s.copy(), tar)
                if tmp == tar:
                    return tar
                ans.append(tmp)
        
    if len(ans) == 0:
        return sum(s)
    return max(ans)

tarSet = set([])
for i in range(height):
    for s in arr[i]:
        tarSet.add(s)
k = len(tarSet)
del tarSet
print(DFS(arr, 0,0, [0]*26, k))
        
