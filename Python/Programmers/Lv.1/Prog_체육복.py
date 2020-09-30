
n = 5
lost = [2,3,4]
reserve = [3,4,5]

def solution(n, lost, reserve):

    losts = set(lost)
    reserves = set(reserve)
    ans = reserves & losts
    losts = losts - ans
    reserves = reserves - ans

    answer = n - len(lost)  # 5 - 3 = 2

    for i in reserves:
        if i-1 in losts:
            losts.pop()
            answer += 1
        elif i+1 in losts:
            losts.pop()
            answer += 1
    return answer + len(ans)


print(solution(n,lost,reserve))

### 한줄쏘쓰
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost] # lost 에는 없는데 reserve 에는 있는거
    _lost = [l for l in lost if l not in reserve] # reserve 에는 없는데 lost에는 있는거
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost) # lost, reserve 중복인 애는 잃어버린 애가 아니네. 그냥 reserve도 아니고, lost도 아닌 애 취급
