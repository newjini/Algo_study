def solution(n):
    answer = []
    ans = list(str(n))
    ans.reverse()
    for i in ans:
        answer.append(int(i))
    return answer


print(solution(n=12345))


### 한줄쏘쓰
def digit_reverse(n):
    return list(map(int, reversed(str(n))))