import sys
read = sys.stdin.readline

N = int(input())
rgb = [[0] * (N) for _ in range(N)]
for i in range(N):
    rgb[i] = list(map(int, read().rstrip().split(' ')))

if N == 1:
    print(min(rgb[0]))
else:
    r = [0] * N
    g = [0] * N
    b = [0] * N
    for i in range(N):
        r[i] = rgb[i][0]
        g[i] = rgb[i][1]
        b[i] = rgb[i][2]

    for i in range(1, N):
        r[i] = min(r[i]+g[i-1], r[i]+b[i-1])
        g[i] = min(g[i]+r[i-1], g[i]+b[i-1])
        b[i] = min(b[i]+r[i-1], b[i]+g[i-1])

    res = min(r[N-1], g[N-1], b[N-1])
    print(res)


