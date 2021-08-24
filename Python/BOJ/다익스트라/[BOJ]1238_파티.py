import sys, heapq
read = sys.stdin.readline

# 단방향,
n, m, x = map(int, input().split())
graphGo = [[] for _ in range(n+1)]
graphCome = [[] for _ in range(n+1)]

for i in range(m):
    a, b, t = map(int, read().rstrip().split())
    graphGo[a].append((b,t))
    graphCome[b].append((a, t))

def dijkstra(graph):
    dist = [float('inf')] * (n+1)
    q = []
    dist[x] = 0
    heapq.heappush(q, (dist[x], x))

    while q:
        nowCost, now = heapq.heappop(q)
        if dist[now] < nowCost:
            continue

        for next, nextCost in graph[now]:
            if dist[next] > dist[now] + nextCost:
                dist[next] = dist[now] + nextCost
                heapq.heappush(q, (dist[next], next))
    return dist

arr1 = dijkstra(graphGo)
arr2 = dijkstra(graphCome)
answer = 0
for i in range(1, n+1):
    if answer < arr1[i] + arr2[i]:
        answer = arr1[i] + arr2[i]
print(answer)
