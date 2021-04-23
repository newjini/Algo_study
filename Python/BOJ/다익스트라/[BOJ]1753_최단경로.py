import sys, heapq
read = sys.stdin.readline
v,e = map(int, read().rstrip().split(' ')) # v : 정점개수, e : 간선개수
k = int(input()) # k : 시작 정점

graph = [[] for _ in range(v+1)]
dis = [int(1e9)] * (v+1) # 거리 배열 

for i in range(e):
    u,v,w = map(int, read().rstrip().split(' '))
    graph[u].append((v, w))


def dikjstra(start, w):
    queue = []
    heapq.heappush(queue, (w,start))  # w : 가중치, start : 정점
    dis[start] = 0
    
    while queue:
        weight, v = heapq.heappop(queue)
        # 현재 pop한 weight가 기존 dis[v] 보다 크다면 넘김
        if weight > dis[v]:
            continue

        if graph[v]: # graph[v]가 존재한다면,
            for nextV, nextWeight in graph[v]: # 그래프에는 (정점,가중치)
                # nextWeight + dis[v]가 dis[nextV]보다 작다면 update.
                if nextWeight + dis[v] < dis[nextV]:
                    dis[nextV] = nextWeight + dis[v]
                    heapq.heappush(queue,(dis[nextV], nextV)) # update된 dis[nextV] 로 dis 탐색하기 위해

dikjstra(k,0)
for i in dis[1:]:
    print(i if i != 1e9 else "INF")