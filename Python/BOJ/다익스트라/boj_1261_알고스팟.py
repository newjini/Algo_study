import heapq
import sys
read = sys.stdin.readline
m, n = map(int, read().rstrip().split(' '))
arr = [] 
dy = [ -1, 0, 0, 1] ## 상 좌 우 하 
dx = [ 0, -1, 1, 0] 

for i in range(n):
    arr.append(list(map(int, read().rstrip()))) # 1인 경우에만 벽 뿌수는거 세기


INF = int(1e9)
distance =[[INF] * (m) for _ in range(n)] 
visited = [[False] * (m) for _ in range(n)]
distance[0][0] = 0

q = []
heapq.heappush(q, [0, 0,0]) # start : (0,0), end : (n, n)

while q:
    weight, y, x = heapq.heappop(q)
    if(visited[y][x]):
        continue
    visited[y][x] = True
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
         # 방문 안했는데 벽일 경우만 세기
        if ny >= 0 and ny < n and nx >= 0 and nx < m:
            if not visited[ny][nx]:
                if distance[ny][nx] > distance[y][x] + arr[ny][nx]:
                    distance[ny][nx] = distance[y][x] + arr[ny][nx]
                    heapq.heappush(q, [distance[ny][nx], ny, nx])

print(distance[n-1][m-1])
                 



