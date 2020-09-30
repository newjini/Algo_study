def solution(x):
    answer = True
    x = str(x)
    num = 0
    for i in x:
        num += int(i)
    if int(x) % num == 0:
        answer = True
    else:
        answer = False
    return answer



print(solution(x=10))
print(solution(x=12))
print(solution(x=11))
print(solution(x=13))

### 한줄쏘쓰
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0