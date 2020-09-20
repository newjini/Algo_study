def solution(arr):
    answer = []
    ans = sorted(arr, reverse=True)
    res = ans[-1]
    for i in range(len(arr)):
        if arr[i] != res:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)
    return answer

def solution2(arr):
    answer = []
    res = min(arr)
    for i in range(len(arr)):
        if arr[i] != res:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)
    return answer


print(solution(arr=[4,3,1,1,1,3,2,1]))
print(solution(arr=[2,3,1,1]))
print(solution(arr=[1,5,7,3,2,6]))
print(solution(arr=[10]))


### 한줄쏘쓰
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]