arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])

    return answer


print(solution(arr))


### 한 줄 쏘쓰
def oneline(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
