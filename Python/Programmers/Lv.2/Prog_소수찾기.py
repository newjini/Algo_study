import itertools

def solution(numbers):
    sea = []
    for i in range(len(numbers)+1):
        a = list(map(list,itertools.permutations(numbers, i+1)))
        for j in a:
            b =''.join(j)
            sea.append(b)

    sea = set(map(int,sea))
    sea = sea - {0, 1}

    for i in range(2, max(sea)+1):
        for j in range(2*i, max(sea)+1, i):
            if j in sea:
                sea.remove(j)

    return len(sea)

print(solution(numbers="17"))
print(solution(numbers="011"))
#print(solution(numbers="0152391"))


### 한줄쏘
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
