from collections import deque
# 1. P 위치들 저장
# 2. BFS 돌려서 2 이하인데 P 마주치면 return 0
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def BFS(arr, place):
    global dy, dx
    visited = [[False for _ in range(5)] for _ in range(5)]
    
    for x, y in arr:
        cnt = 0
        visited[x][y] = True
        q = deque([])
        q.append((x,y, cnt))
        while q:
            a, b, c = q.popleft() # BFS 는 deque ㅠㅠㅠㅠㅠㅠ 
            
            
            for k in range(4):
                na = dy[k] + a
                nb = dx[k] + b

                if c < 2: # 거리가 2 이하인 조건.
                    if 0 <= na < 5 and 0 <= nb < 5 and not visited[na][nb]:
                        if place[na][nb] == 'O':
                            visited[na][nb] = True
                            q.append((na,nb, c+1))
                        if place[na][nb] == 'P':
                            return 0
    return 1

def solution(places):
    global dy, dx
    answer = []
    
    for place in places: # 대기실 하나를 뽑아서
        IsClose = True 
        arr = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    arr.append((i,j))
        answer.append(BFS(arr, place))
    
    return answer