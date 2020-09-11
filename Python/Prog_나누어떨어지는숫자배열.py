
arr = [5,9,7,10]
divisor = 5
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if not answer:
        answer.append(-1)

    return answer

### 한줄쏘쓰
def oneline(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
