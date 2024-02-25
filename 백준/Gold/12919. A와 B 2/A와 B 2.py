from sys import stdin

def dfs(end, start):

    if len(end) == len(start):
        return end == start

    ans = False

    if end[0] == 'B':
        ans = dfs(end[1:][::-1], start)
        if ans:
            return ans
    if end[-1] == 'A':
        ans = dfs(end[:-1], start)
    return ans
start = stdin.readline().removesuffix('\n')
end = stdin.readline().removesuffix('\n')
print(int(dfs(
    end, start
)))
