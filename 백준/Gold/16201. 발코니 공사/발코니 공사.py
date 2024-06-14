from sys import stdin

p = 1_000_000_007


r,c,k = map(int, stdin.readline().split())

t = {}

def divRow(row, idx):
    acc = 0
    ret = []
    for i, r in enumerate(row):
        if r < 0:
            acc -= r
            ret.append(r)
            continue
        if acc + 1 == idx:
            if len(ret) and ret[-1] < 0:
                ret[-1] -= 1
            else:
                ret.append(-1)
            if r-1 > 0:
                ret.append(r-1)
            ret += row[i+1:]
            return ret
        if acc + r > idx:
            ret.append(idx-acc-1)
            ret.append(-1)
            ret.append(r-idx+acc)
            ret += row[i+1:]
            return ret
        if acc + r == idx:
            ret.append(r-1)
            ret.append(-1)
            ret += row[i+1:]
            return ret
        ret.append(r)
        acc += r
    return ret


def calc(row):
    ans = 1
    cnt = 0

    for r in row:
        if r < 0:
            continue
        cnt += r//2
        if r > 1 and r%2:
            ans *= (r//2 + 1)
            ans %= p
    return (ans, cnt)


ans,cnt = 1, 0
for _ in range(k):
    row, col = map(int, stdin.readline().split())
   
    t[row-1] = divRow(t.get(row-1,[c]), col)

    # print(t)

for key in t.keys():
    ta, tc = calc(t[key])
    ans *= ta
    ans %= p
    cnt += tc

cnt += (c//2) * (r - len(t.keys()))
if c%2:
    ans *= pow(c//2+1, r-len(t.keys()), p)
    ans %= p
    
print(cnt, ans)