import copy
def solution(str1, str2):

    arr = []
    for i in range(len(str1)-1):
        res = str1[i]+str1[i+1]
        if res.isalpha():
            arr.append(res.lower())

    arr2 = []
    for i in range(len(str2)-1):
        res = str2[i]+str2[i+1]
        if res.isalpha():
            arr2.append(res.lower())
    
    inter = 0
    tmp = copy.deepcopy(arr2)
    for i in range(len(arr)):
        if arr[i] in tmp:
            inter += 1
            tmp.remove(arr[i])
    
    union = len(arr)+len(arr2) - inter
    
    if inter == 0 and union == 0:
        answer = 65536
    else:
        answer = int(inter / union * 65536)

    return answer