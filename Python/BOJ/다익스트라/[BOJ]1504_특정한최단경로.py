# 다시 풀어보기 # 

import sys, heapq
read = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a, b, c = map(int, read().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, read().rstrip().split())

def dijkstra(start):
    dist = [int(1e9)] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q,(dist[start], start))

    while q:
        nowCost, nowNode = heapq.heappop(q)
        
        if nowCost > dist[nowNode]:
            continue

        for nextNode, nextCost in graph[nowNode]:
            if dist[nowNode] + nextCost < dist[nextNode]:
                dist[nextNode] = dist[nowNode] + nextCost
                heapq.heappush(q, (dist[nextNode], nextNode))
    return dist

from_1 = dijkstra(1) # 1부터 시작하는 dijkstra
from_v1 = dijkstra(v1) # v1부터 시작하는 dijkstra
from_v2 = dijkstra(v2) # v2부터 시작하는 dijkstra

path1 = from_1[v1] + from_v1[v2] + from_v2[n] # 1~v1, v1~v2, v2~n 까지의 최단거리
path2 = from_1[v2] + from_v2[v1] + from_v1[n] # 1~v2, v2~v1, v1~n 까지의 최단거리

result = min(path1, path2)

if result < int(1e9):
    print(result)
else:
    print(-1)
