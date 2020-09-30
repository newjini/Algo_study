
a=3
b=5
def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a,b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i
    return answer

### 한줄쏘쓰
def solution2(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a
    
    return sum(range(a,b+1))