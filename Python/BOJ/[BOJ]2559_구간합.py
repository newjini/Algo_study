import sys
read = sys.stdin.readline 
n, k = map(int, read().rstrip().split(' '))
arr = list(map(int, read().rstrip().split(' ')))

sum = [0] * (n+1)

maxi = -(1e9)
for i in range(n):
    sum[i+1] = sum[i] + arr[i]

for i in range(k, n+1):

    maxi = max(maxi ,sum[i] - sum[i-k])
print(maxi)
