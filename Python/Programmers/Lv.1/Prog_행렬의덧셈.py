import copy
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = copy.deepcopy(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = 0
            
    for i, j in zip(range(len(arr1)), range(len(arr2))):
        for a, b in zip(range(len(arr1[i])), range(len(arr2[j]))):
            answer[i][a] = arr1[i][a] + arr2[j][b]

    return answer

print(solution(arr1,arr2))


### 한줄쏘쓰
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer