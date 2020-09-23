
def solution(d, budget):

    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] >= 0:
            answer += 1
            budget = budget - d[i]
        else:
            break
    return answer

#맥시멈


### 한줄쏘쓰

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


print(solution(d=[1,3,2,5,4], budget=9))
print(solution(d=[2,2,3,3], budget=10))

