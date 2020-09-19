import math

def solution(n):
    answer = math.sqrt(n)
    if n % answer == 0:
        answer = int(math.pow((answer + 1), 2))
    else:
        answer = -1
    return answer



print(solution(n=121))
print(solution(n=3))


### 한줄쏘쓰
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'