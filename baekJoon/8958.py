for _ in range(int(input())):
    ans = 0
    tmp = 0
    for s in input():
        if s =='X':
            tmp = 0
        elif s=='O':
            tmp += 1
            ans += tmp
    print(ans)