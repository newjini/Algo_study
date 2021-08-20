
import sys, heapq
import copy

read = sys.stdin.readline

n = int(input())
m = int(input())

city = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
dist = [int(1e9)] * (n+1)
for i in range(m):
    a, b, Cost = map(int, read().rstrip().split())
    graph[a].append((Cost, b))

start, end = map(int, read().rstrip().split())

q = []
heapq.heappush(q, (0, start)) # 비용먼저
dist[start] = 0
# city[start].append(start)
while q:
    cost, now = heapq.heappop(q)

    if cost > dist[now]:
        continue
    
    # city[now].append(now)

    if now == end:
        break

    for nextCost, next in graph[now]:
        if dist[next] > dist[now] + nextCost:
            dist[next] = dist[now] + nextCost
            heapq.heappush(q, (dist[next], next))
            
            # city[next] = copy.deepcopy(city[now])
            city[next] = now
            # city[next] = []
            # for i in city[now]:
            #     city[next].append(i)
            # city[next].append(next)

# 뒤집는 부분!!!!
prev = city[end]
answer = [end]
while prev != start:
    answer.append(prev)
    prev = city[prev]
answer.append(start)

print(dist[end])
print(len(answer))
print(' '.join(map(str, answer[::-1])))

# print(dist[end])
# print(len(city[end]))
# print(' '.join(map(str, city[end])))
