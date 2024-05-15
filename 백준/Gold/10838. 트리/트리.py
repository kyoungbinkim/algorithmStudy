from sys import stdin

n, k = map(int, stdin.readline().split())
tree = [[0, 0] for _ in range(n)]
# tree = [[0,0], [0,0], [1,0], [1,0],[2,0]]
def lca(a, b):
    ap, bp = set(), set()

    na, nb = a,b

    while na != 0 or nb != 0:
        if na != 0:
            if na in bp:
                return na
            ap.add(na)
            na = tree[na][0]
        if nb != 0:
            if nb in ap:
                return nb
            bp.add(nb)
            nb = tree[nb][0]
    return 0

for _ in range(k):
    cmd = list(map(int, stdin.readline().split()))

    # paint
    if cmd[0] == 1:
        LCA = lca(cmd[1], cmd[2])
        color = cmd[3]

        while cmd[1] != LCA:
            tree[cmd[1]][1] = color
            cmd[1] = tree[cmd[1]][0]
        while cmd[2] != LCA:
            tree[cmd[2]][1] = color
            cmd[2] = tree[cmd[2]][0]

    # move
    elif cmd[0] == 2:    
        a,b = cmd[1], cmd[2]
        tree[a][0] = b

    # count
    elif cmd[0] == 3:
        cnt =set()
        LCA = lca(cmd[1], cmd[2])

        while cmd[1] != LCA:
            cnt.add(tree[cmd[1]][1])
            cmd[1] = tree[cmd[1]][0]
        while cmd[2] != LCA:
            cnt.add(tree[cmd[2]][1])
            cmd[2] = tree[cmd[2]][0]
        print(len(cnt))

