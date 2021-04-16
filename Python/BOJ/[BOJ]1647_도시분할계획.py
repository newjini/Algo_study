import sys, heapq
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' ')) 
# N : 정점, M : 간선 수
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a, b, c = map(int, read().rstrip().split(' '))
    graph[a].append([b, c])
    graph[b].append([a, c])

queue = []
heapq.heappush(queue, (0, 1)) # (가중치, 정점) 정점 : 1, 가중치 0

res = 0
maxi = 0
while queue:
    cost, now = heapq.heappop(queue)
    if visited[now]:
        continue
    visited[now] = True
    res += cost
    maxi = max(maxi, cost)
    for val in graph[now]:
        next, nextCost = val
        if not visited[next]:
            heapq.heappush(queue, (nextCost,next))

print(res - maxi)