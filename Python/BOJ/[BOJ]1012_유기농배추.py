# BOJ 1012 - 유기농 배추 [ DFS 로 풀음 ]
import sys
read = sys.stdin.readline
dy = [ -1, 0, 0, 1]
dx = [ 0, -1, 1, 0]
def DFS(y, x):
    arr[y][x] = 2
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < m and nx >= 0 and nx < n:
            if arr[ny][nx] == 1:
                DFS(ny,nx)
tc = int(input())
for t in range(tc):
    m, n, k = map(int, read().rstrip().split(' '))
    cnt = 0

    arr = [[0] * n for _ in range(m)]
    for i in range(k):
        a, b = map(int, read().rstrip().split(' '))
        arr[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                DFS(i,j)
    print(cnt)
