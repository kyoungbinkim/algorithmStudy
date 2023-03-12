from sys import stdin

move = [[1,0], [0,1],  [0,-1], [-1,0]]
n,m = map(int, stdin.readline().split())
arr = []

for _ in range(n):
    arr.append([x for x in stdin.readline().replace('\n','')])

def DFS(x,y,visit:set):
    ans = 0
    
    for dx, dy in move:
        x_, y_ = x+dx, y+dy

        if 0<= x_ < n and  0<= y_ < m and arr[x_][y_] not in visit:
            visit.add(arr[x_][y_])
            tmp = DFS(x_, y_, visit)
            visit.discard(arr[x_][y_])
            ans = tmp if tmp > ans else ans
    
    if ans == 0:
        return len(visit)
    return ans

print(DFS(0,0, set(arr[0][0])))