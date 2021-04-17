import sys, heapq
read = sys.stdin.readline

N = int(input()) # 정점 수
M = int(input()) # 간선 수
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a, b, c = map(int, read().rstrip().split(' '))
    graph[a].append([b, c])
    graph[b].append([a, c])

queue = []
heapq.heappush(queue, (0, 1)) # ( 가중치, 정점 ) 정점1 의 가중치가 0 
res = 0
while queue:
    cost, now = heapq.heappop(queue)
    # 방문체크 먼저!
    if visited[now]:
        continue
    # 응 방문안했어
    visited[now] = True
    res += cost
    # 연결된 애만 가져와라
    for val in graph[now]:
        # 응 나야
        next, nextCost = val
        # 연결 안된 애만
        if not visited[next]:
            heapq.heappush(queue,(nextCost, next))

print(res)