
from itertools import combinations
from collections import Counter
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    # 조합하기
    for cour in course:
        dic = defaultdict()
        combis = []
        res = 0
        for order in orders:
            order = sorted(order)
            combis += combinations(order, cour)
        dic = Counter(combis).most_common()
        maxi = 0
        for arr, n in dic:
            if n >= 2 and maxi <=n:
                maxi = n
                answer.append(arr)
    res = []
    for ans in answer:
        ans = ''.join(ans)
        res.append(ans)
    res.sort()
    return res