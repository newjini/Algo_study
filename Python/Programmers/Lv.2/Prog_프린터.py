from collections import deque

def solution(priorities, location):
    
    answer = 0
    
    q = deque(priorities)
    line = []
    order = deque([])
    idx = 0
    for val in priorities:
        order.append([val, idx])
        idx += 1
    while q:
        maxi = max(q)
        now = q.popleft()
        nows = order.popleft()
        if now == maxi:
            line.append(nows)
        else:
            q.append(now)
            order.append(nows)
    
    for idx, val in enumerate(line):
        val_v, val_k = val
        if val_k == location:
            answer = idx+1
        
    return answer