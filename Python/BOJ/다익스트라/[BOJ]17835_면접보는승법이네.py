import sys, heapq
read = sys.stdin.readline

n, m, k = map(int, input().split())
graph= [[] for _ in range(n+1)]
for i in range(m):
    u, v, c = map(int, read().rstrip().split())
    graph[v].append((u,c))

dest = list(map(int, read().rstrip().split())) # 면접장 위치
dist = [float('inf')] * (n+1)
q = []
for i in dest:
    dist[i] = 0
    heapq.heappush(q, (dist[i], i))

def dijkstra(): 

    while q:
        nowCost, now = heapq.heappop(q)
        if dist[now] < nowCost:
            continue
        
        for next, nextCost in graph[now]:
            if dist[next] > dist[now] + nextCost:
                dist[next] = dist[now] + nextCost
                heapq.heappush(q, (dist[next], next))

answer = [0, 0]
dijkstra()

for i in range(1, n+1):
    if dist[i] > answer[1]:
        answer[1] = dist[i]
        answer[0] = i
print('\n'.join(map(str, answer)))

