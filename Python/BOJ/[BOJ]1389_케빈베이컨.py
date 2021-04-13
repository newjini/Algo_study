# BOJ 1389 케빈 베이컨의 6단계 법칙 
# 풀이 : 플로이드
import sys
read = sys.stdin.readline
n, m = map(int, read().rstrip().split(' ')) # n : 유저 수, m : 친구 관계 수
arr = [[int(1e9)] * n for _ in range(n)] # nxn 배열
for i in range(m):
    a, b = map(int, read().rstrip().split(' '))
    arr[a-1][b-1] = 1 # a 와 b는 친구사이
    arr[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] != 1e9 and arr[k][j] != 1e9:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

res = [0] * n
ans = int(1e9)
for i in range(n):
    for j in range(n):
        if i != j:
            res[i] = res[i] + arr[i][j]
    if ans > res[i]:
        ans = res[i]
        result = i

print(result+1)