def solution(prices):
    answer = [0 for _ in range(len(prices))]
    # answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j] < prices[i]:
                answer[i] = j-i
                break
            else:
                answer[i] = len(prices)-(i+1)
                continue

    return answer

print(solution(prices=[1,2,3,2,3]))
print(solution(prices=[3,4,2,6,5]))


### 한줄쏘쓰
def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer