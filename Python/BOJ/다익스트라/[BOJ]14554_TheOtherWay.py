# 다시 풀어보기 # 

import sys, heapq
read = sys.stdin.readline

n, m, s, e = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, read().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [float('inf')] * (n+1)
count = [0] * (n+1)


def dijkstra(s):
    q = []
    dist[s] = 0
    count[s] = 1 # 경우의 수 세기 시작
    heapq.heappush(q, (dist[s], s))

    while q:
        nowCost, now = heapq.heappop(q)

        if dist[now] < nowCost:
            continue
        
        for next, nextCost in graph[now]:
            if dist[next] > dist[now]+nextCost:
                dist[next] = dist[now]+nextCost
                count[next] = count[now]
                heapq.heappush(q, (dist[next], next))

            # 이미 방문했던 곳의 최단거리가 현재 최단거리와 같다면
            elif dist[next] == dist[now] + nextCost:
                count[next] = (count[next]+count[now]) % 1000000009
dijkstra(s)

print(count[e])
