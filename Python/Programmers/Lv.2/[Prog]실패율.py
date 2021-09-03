import collections

def solution(N, stages):

    ans = collections.defaultdict(int)
    arr = collections.Counter(stages)
    
    num = len(stages)
    for i in range(1, N+1):
        fail = arr.get(i)
        if fail is None:
            fail = 0
            ans[i] = 0
            continue
        ans[i] = float(fail / num)
        num -= fail

    ans = sorted(ans.items(), key=lambda x:-x[1])

    answer = [a[0] for a in ans]
    
    return answer