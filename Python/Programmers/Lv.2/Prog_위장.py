from collections import Counter
from functools import reduce

def solution(clothes):
    cate = dict()
    print(cnt)
    for i in clothes:
        arr = cate.get(i[1], [])
        arr.append(i[0])
        cate[i[1]] = arr
    ans = 1

    for i in cate.keys():
        ans = ans * (len(cate[i]) + 1)
    return ans - 1


print(solution(clothes=[["yellow_hat", "headgear"],
                        ["blue_sunglasses", "eyewear"],
                        ["green_turban", "headgear"]]))
print(solution(clothes=[["crow_mask", "face"],
                        ["blue_sunglasses", "face"],
                        ["smoky_makeup", "face"]]))
print(solution(clothes=[["yello", "headgear"],
                        ["blue", "eyewear"],
                        ["green", "face"]]))


### 한줄쏘쓰

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer