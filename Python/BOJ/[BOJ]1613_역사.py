import sys
read = sys.stdin.readline

n, k = map(int, read().rstrip().split(' ')) # n: 사건 개수, k : 사건전후관계개수
arr =[[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, read().rstrip().split(' '))
    arr[a-1][b-1] = -1
    arr[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                if arr[i][k] == -1 and arr[k][j] == -1:
                    arr[i][j] = -1 # 앞의 사건이 먼저 일어났다면 1 로 해야함.
                    arr[j][i] = 1
                elif arr[j][k] == 1 and arr[k][i] == 1:
                    arr[j][i] = 1  # 뒤의 사건이 먼저 일어났다면 1 로 해야함. 
                    arr[i][j] = -1

## 출력
s = int(input()) # s : 알고싶은 사건 쌍의 수
for i in range(s):
    a, b = map(int, read().rstrip().split(' '))
    print(arr[a-1][b-1])