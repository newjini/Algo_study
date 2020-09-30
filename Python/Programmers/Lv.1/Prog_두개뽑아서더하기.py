

def solution(numbers):
    answer = []
    for num1, i in enumerate(numbers):
        for num2, j in enumerate(numbers):
            if num1 != num2:
                if i+j not in answer:
                    answer.append(i+j)
    answer.sort()
    return answer


print(solution(numbers=[2,1,3,4,1]))
print(solution(numbers=[5,0,2,7]))