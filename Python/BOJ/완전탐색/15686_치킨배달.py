import sys
import itertools
read = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, read().rstrip().split())) for _ in range(n)]

# 1. 치킨집 저장
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i,j])

# 2. 치킨집 위치 조합
realChicken = list(itertools.combinations(chicken, m))

# 3. 치킨거리 구하기
ans = int(1e9)
for k in realChicken: # 구해진 치킨집 위치
    distance = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: # 집이면 최소 치킨 거리 구하기
                cdist = int(1e9)
                for ci, cj in k:
                    dist = abs(i-ci) + abs(j-cj)
                    cdist = min(cdist, dist)
                distance.append(cdist) # 작은 치킨 거리 넣기
    ans = min(ans, sum(distance))
print(ans)