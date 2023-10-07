from collections import deque

def parsePlan(plan):
    start = int(plan[1].split(':')[0]) * 60 + int(plan[1].split(':')[1])
    end = start + int(plan[2])
    
    return (start, end, plan[0])
    
def solution(plans):
    p,answer = [],[]
    
    for plan in plans:
        p.append(parsePlan(plan))
    p.sort()
    print(p)
    
    schedule, wait = deque(p), deque()
    endTime = schedule[0][0]
    
    while len(schedule) or len(wait):
        # print(schedule)
        # print(wait, endTime, answer)
        # print()
        if len(wait) and len(schedule) == 0:
            while len(wait):
                answer.append(wait.pop()[1])
            break
        elif len(wait) and  endTime < schedule[0][0]:
            waitTime = wait.pop()
            nowSchedule = (endTime, endTime + waitTime[0], waitTime[1])
        elif len(schedule):
            nowSchedule = schedule.popleft()
        
        if len(schedule) == 0:
            answer.append(nowSchedule[2])
        
        elif nowSchedule[1] <= schedule[0][0]:
            answer.append(nowSchedule[2])
            endTime= nowSchedule[1]
            
            if len(wait):
                pass
        else:
            remain = nowSchedule[1] - schedule[0][0]
            endTime = schedule[0][0]
            wait.append((remain, nowSchedule[2]))
    # print(schedule)
    # print(wait, endTime, answer)
    # print()
        
    
    
    
    return answer