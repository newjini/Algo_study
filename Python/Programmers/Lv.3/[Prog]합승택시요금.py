from collections import defaultdict
from heapq import heappush, heappop

graph = defaultdict(list)
INF = float('inf')


def run(n, start, end):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)
        if dist[node] < cost:
            continue

        for nxt_n, c in graph[node]:
            nxt_c = cost + c
            if dist[nxt_n] > nxt_c:
                dist[nxt_n] = nxt_c
                heappush(q, (nxt_c, nxt_n))
    return dist[end]

def solution(n, s, a, b, fares):
    answer = INF
    for fare in fares:
        u, v, c = fare
        graph[u].append((v, c))
        graph[v].append((u, c))
    # 아예 합승하지 않은 경우
    answer = run(n,s,a) + run(n,s,b)
    # 특정 노트까지 합승
    for node in range(1, n+1):
        answer = min(answer, run(n, s, node) + run(n, node, a) + run(n, node, b))
    print(answer)
    return answer