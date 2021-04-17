import sys, heapq
read = sys.stdin.readline
# 함수 나눈거 실패 히히

N, M = map(int, read().rstrip().split(' ')) 
# N : 정점, M : 간선 수
graph = [[] for _ in range(N+1)]
queue = []
visited = [False] * (N+1)
for i in range(M):
    a, b, c = map(int, read().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

heapq.heappush(queue, (0, 1)) # (가중치, 정점) 정점 : 1, 가중치 0

def prim():
    last = 0
    result = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if visited[now]:
            continue
        visited[now] = True
        last = max(last, cost)
        result += cost

        for val in graph[now]:
            next, nextCost = val
            if not visited[next]:
                heapq.heappush(queue, (nextCost,next))
    return result-last

res = prim()
print(res)