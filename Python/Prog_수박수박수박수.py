

def solution(n):
    answer = ''
    for i in range(n // 2):
        answer = answer + '수박'
        if n % 2 != 0:
            answer = answer + '수'

    return answer

print(solution(3))


### 한줄쏘쓰
def water_melon(n):
    s = "수박" * n
    return s[:n]