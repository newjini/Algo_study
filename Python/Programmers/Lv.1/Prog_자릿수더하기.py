

def solution(n):
    a = str(n)
    answer = 0

    for i in a:
        answer += int(i)


    return answer


print(solution(n=123))

### 한줄 쏘쓰
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    return sum(map(int,str(number)))