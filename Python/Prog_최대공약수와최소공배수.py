

def solution(n, m):
    mini = 0
    if n > m:
        n, m = n , m
    else:
        n, m = m, n
    ## 최대공약수 구하기
    if n % m == 0:
        mini = m
    else:
        for i in range(1, m):
            if n % i == 0 and m % i ==0:
                mini = i
    ## 최소공배수 구하기
    maxi = mini * (n // mini) * (m // mini)
    answer = [mini, maxi]
    return answer



print(solution(n=3,m=12))
print(solution(n=2,m=5))

### 한줄쏘쓰
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]