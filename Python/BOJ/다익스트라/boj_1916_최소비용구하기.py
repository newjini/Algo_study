import heapq
import sys
read = sys.stdin.readline
# start : A도시 , end : B도시

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
INF = int(1e9)
for i in range(m):
    busA, busB, weight = map(int, read().rstrip().split(' '))
    arr[busA].append([busB, weight])

start, end = map(int, read().rstrip().split(' '))

visited = [False] * (n+1)
distance = [INF] * (n+1)
distance[start] = 0

q = []
heapq.heappush(q, (0, start)) # 앞 : 비용, 뒤 : 인덱스

while q:
    weight , now = heapq.heappop(q)
    if visited[now]:
        continue

    visited[now] = True

    for next in arr[now]: # next[0] : next.no, next[1] : next.weight
        
        if not visited[next[0]] and distance[next[0]] > distance[now] + next[1]:
            
            distance[next[0]] = distance[now] + next[1]
            heapq.heappush(q, (distance[next[0]], next[0]))

print(distance[end])
