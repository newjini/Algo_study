def solution(n):
    num = [1, 2, 4]
    answer = []
    while(n!= 0):
        rest = n % len(num)
        if rest == 0:
            n = n - 1
        n = n // len(num)
        answer.append(num[rest-1])
    answer.reverse()
    return ''.join(map(str, answer))


# print(solution(n=5))
print(solution(n=6))
# print(solution(n=7))
# print(solution(n=12))
# print(solution(n=15))


### 한줄쏘쓰
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
