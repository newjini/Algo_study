def solution(N, stages):
    ### 마지막 단계를 성공한 사람은 실패한게 아니니까 아예 제외
    ans = {}
    step = {}
    rest = len(stages) # 남은사람
    stages.sort()
    for i in range(N+1):
        step[i] = stages.count(i+1)
    for i in range(N):
        if step[i] == 0:
            cal = 0
        else:
            cal = step[i] / rest

        ans[i+1] = cal
        rest -= step[i]

    ans = sorted(ans, key=lambda k :ans[k], reverse=True)
    return ans


print(solution(N=5,stages=[2,1,2,6,2,4,3,3]))
print(solution(N=4,stages=[4,4,4,4,4]))

### 한줄쏘쓰
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)