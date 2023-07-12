from sys import stdin

dir = {
    1 : [1,0],
    2 : [-1,0],
    3 : [0,-1],
    4 : [0,1]
}

n = int(stdin.readline())

plots = []

for i in range(6):
    direction, length = map(int, stdin.readline().split())
    if len(plots) == 0:
        plots.append([dir[direction][0] * length, dir[direction][1] * length])
        continue

    plots.append([plots[-1][0] + dir[direction][0] * length, plots[-1][1] + dir[direction][1] * length])

# print(plots)

max_x = max(m[0] for m in plots)
min_x = min(m[0] for m in plots)
max_y = max(m[1] for m in plots)
min_y = min(m[1] for m in plots)

# print(max_x, min_x, max_y, min_y)

ans = abs(max_x - min_x) * abs(max_y - min_y)

min_plots = []
for x,y in plots:
    if x in [max_x, min_x] and y in[max_y, min_y]:
        continue
    min_plots.append([x,y])

wid = abs(min_plots[0][0] - min_plots[1][0]) if min_plots[0][0] - min_plots[1][0] != 0 else abs(min_plots[0][0] - min_plots[2][0])
hig = abs(min_plots[0][1] - min_plots[1][1]) if min_plots[0][1] - min_plots[1][1] != 0 else abs(min_plots[0][1] - min_plots[2][1])

# print(min_plots, wid, hig, ans)

ans = ( ans - wid * hig ) * n
print(ans)
