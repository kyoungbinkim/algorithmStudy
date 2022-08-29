import sys
sys.setrecursionlimit(10**9)

Dict = {0:1, 1:2}
def calc(n, p, q):
    if n == 0:
        return 1
    
    if Dict.get(n//p) == None:
        first = calc(n//p, p, q)
        Dict.update({n//p : first})
    else:
        first = Dict.get(n//p)

    if Dict.get(n//q) == None:
        second = calc(n//q, p, q)
        Dict.update({n//q : second})
    else:
        second = Dict.get(n//q)
    
    return first+second
    
N,P,Q = map(int, input().split())
print(calc(N,P,Q))