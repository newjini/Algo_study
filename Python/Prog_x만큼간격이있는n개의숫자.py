def solution(x, n):
    answer = [i*x for i in range(1,n+1)]
    return answer



print(solution(x=2,n=5))
print(solution(x=4,n=3))
print(solution(x=-4,n=2))

### 한줄쏘쓰
def number_generator(x, n):
    return [i * x + x for i in range(n)]