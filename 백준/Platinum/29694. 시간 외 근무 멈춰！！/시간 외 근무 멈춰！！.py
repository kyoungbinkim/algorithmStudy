from sys import stdin
DAY, WKDN, WORK_DAY, OVR_DAY, OVR_WKND = range(5)

n, a,b, m = map(int, stdin.readline().split())

s = sorted([list(map(int ,stdin.readline().split())) for _ in range(n)])

logs =[0 for _ in range(5)]
total_work = 0

for i,(d,t) in enumerate(s):
    total_work += t

    diff_day = d//7 * 5 + (5 if d%7 ==6 else d%7 ) - logs[DAY]
    diff_wknd= d - diff_day - logs[DAY] - logs[WKDN] 
    logs[DAY] +=  diff_day
    logs[WKDN] = d - logs[DAY]
    
    if t and logs[WORK_DAY] < logs[DAY]:
        tmp =  min(logs[DAY] - logs[WORK_DAY], t)
        logs[WORK_DAY] += tmp
        
        t -= tmp
    
    if t and logs[DAY] > logs[OVR_DAY]:
        tmp = min(logs[DAY] - logs[OVR_DAY], t)
        logs[OVR_DAY] += tmp
        
        t -= tmp
    
    # print(f'd: {d}, t:{t}, total_work : {total_work}')
    # print(t)
    
    if t and logs[WKDN] > logs[OVR_WKND]:
        tmp = min(logs[WKDN] - logs[OVR_WKND], t)
        logs[OVR_WKND] += tmp
        
        t -= tmp
    
    # print(f"""
    #       diff_day : {diff_day}
    #       diff_wknd : {diff_wknd}
    #       logs[DAY]  : {logs[DAY] }
    #       logs[WKDN] : {logs[WKDN]}
          
    #       logs[WORK_DAY] : {logs[WORK_DAY]}
          
    #       logs[OVR_DAY] : {logs[OVR_DAY]}
    #       logs[OVR_WKND] : {logs[OVR_WKND]}
    #       total_work : {total_work}
    #       """)
    
    if t > 0:
        print(-1)
        exit()

ans = -1

if logs[OVR_DAY] + logs[OVR_WKND] > logs[DAY] + logs[WKDN]:
    pass

elif a==b==0:
    if m:
        pass
    
    else:
        ans = logs[OVR_WKND]

elif a == 0:
    if m%b == 0 and logs[WKDN] >=  m//b >= logs[OVR_WKND]:
        ans = m // b

elif b == 0:
    if  m%a == 0 and  m//a <=logs[DAY]:
        ans = logs[OVR_WKND]  + logs[OVR_DAY] - m//a

else:
    for _y in range(logs[OVR_WKND], logs[WKDN]+1):
        diff_ovr_wknd = _y - logs[OVR_WKND]
        ovr_day = m - _y * b
        
        
        if ovr_day >= 0 and ovr_day % a == 0 and \
            logs[DAY] >= ovr_day // a >= logs[OVR_DAY] - diff_ovr_wknd:
                ans = _y
                break
            
print(ans)     

'''

ax + by = m
n>= x+y >= ovr
day >= x
wknd >= y

y = (m-ax) / b
b * wknd >= (m-ax) 
ax >=m - b * wknd
x >= ( m - b * wknd ) / a

''' 
    

