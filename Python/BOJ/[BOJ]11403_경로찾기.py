import sys
read = sys.stdin.readline

n = int(input())
arr = [[int(1e9) * n] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, read().rstrip().split(' ')))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
for i in arr:
    for j in i:
        print(j, end=" ")
    print()