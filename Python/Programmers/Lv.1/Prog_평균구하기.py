
def solution(arr):

    if sum(arr) % len(arr) == 0:
        answer = sum(arr) // len(arr)
    else:
        answer = sum(arr) / len(arr)

    return answer


print(solution(arr=[1,2,3,4]))
print(solution(arr=[5,5]))


### 한줄쏘쓰
def average(list):
    return (sum(list) / len(list))