array = [1,5,2,6,3,7,4]
commands =[[2,5,3],[4,4,1],[1,7,3]]

answer = []

def solution(array, *commands):
    for n in commands:
        for a,b,c in n:
            ans = list(sorted(array[a-1:b]))
            res = ans[c-1]
            answer.append(res)
    return answer

print(solution(array, commands))


### 한 줄 쏘쓰
def solution2(array,commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
print(solution2(array,commands))
