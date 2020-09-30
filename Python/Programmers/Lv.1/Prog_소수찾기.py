import math

n = 10


def solution(n):
    ans = {i for i in range(2,n+1)}
    sqrtn = math.sqrt(n)
    for i in range(2,int(sqrtn)+1):
        if i in ans: ### True
            for j in range(i*i, n+1, i):
                if j in ans:
                    ans.remove(j)  ## False
    return len(ans)


print(solution(n))

### 한줄쏘쓰
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)