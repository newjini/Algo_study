import sys, heapq
read = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, read().rstrip().split(' '))

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for i in range(M):
        a, b = map(int, read().rstrip().split(' '))
        graph[a].append([b,1])
        graph[b].append([a,1])
    queue = []
    heapq.heappush(queue, (0, 1)) # 정점1부터 시작하는데 가중치는 0
    mini = 0
    while queue:
        cost, now = heapq.heappop(queue) # 현재 비용, 현재 정점
        if visited[now]:
            continue
        visited[now] = True
        
        mini += cost
        
        for i in graph[now]:
            next, nextCost = i # 헷갈리지 말기 next, nextCost로 담았잖어
            if not visited[next]:
                heapq.heappush(queue, (nextCost, next))
    print(mini)



    

