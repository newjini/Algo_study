import sys
read = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * (k+1) for _ in range(n+1)]
profit = [0] * n # 가치
weight = [0] * n # 무게

for i in range(n):
    w, v = map(int,read().rstrip().split())
    weight[i] = w
    profit[i] = v
for i in range(n+1):
    for w in range(k+1):
        if i==0 or w==0:
            arr[i][w] = 0

        # 현재 들어올 배낭이 들어오긴할때
        elif weight[i] <= w:
            arr[i][w] = max(profit[i]+arr[i-1][w - weight[i]], arr[i-1][w])
        else:
            arr[i][w] = arr[i-1][w]

print(arr[n][k])
