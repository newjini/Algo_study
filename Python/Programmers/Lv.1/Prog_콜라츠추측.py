


def solution(num):
    answer = 0
    while(answer <= 500):
        if num == 1:
            break
        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1


    if num != 1:
        answer = -1

    return answer


print(solution(num=1))
print(solution(num=6))
print(solution(num=16))
print(solution(num=626331))

### 한줄쏘쓰
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1