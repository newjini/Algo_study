def solution(n):
    num = 0
    cnt = 0
    j = 0
    while (num < n):
        arr = []
        j += 1

        for i in range(j, n):
            arr.append(i)
            if sum(arr) >= n:
                if sum(arr) == n:
                    cnt += 1
                break
            continue

        num += 1
    cnt += 1
    return cnt

print(solution(n=15))

### 한줄쏘쓰
def expressions(num):
    return len([i for i in range(1,num+1,2) if num % i == 0])