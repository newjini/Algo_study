# 다시 풀어보기 # 

import sys, heapq
read = sys.stdin.readline

k = int(input()) # 교통비
n = int(input()) # 도시 개수
r = int(input()) # 도로 개수
graph = [[] for _ in range(n+1)]
for i in range(r):
    s,d,l,t = map(int, read().rstrip().split())
    graph[s].append((d,l, t))

dist = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
# 각 노드에 대한 요금 정보
# 해당하는 요금을 가리키는 거리 정보를 저장함.
def dijkstra(l, t):
    q = []
    dist[1][0] = 0 # 거리

    heapq.heappush(q, (l, t, 1))
    
    while q:

        nowDist, nowPrice, now = heapq.heappop(q)
        if nowDist > dist[now][nowPrice]:
            continue

        for next, ndist, nprice in graph[now]:
            nextPrice, nextDist = nowPrice + nprice, nowDist + ndist

            if nextPrice <= k:
                if dist[next][nextPrice] > nextDist:
                    dist[next][nextPrice] = nextDist
                    heapq.heappush(q, ( nextDist, nextPrice, next))

dijkstra(0,0)
ans = min(dist[n])
if ans >= float('inf'):
    print(-1)
else:
    print(ans)


