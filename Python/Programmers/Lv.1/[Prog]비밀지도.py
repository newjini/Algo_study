def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        ans = a | b
        ans = bin(ans)[2:]
        
        ans = ans.zfill(n)
        # 혹은 ans.rjust(n, "0")
        temp = ''
        for i in ans:
            if i == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
            
    return answer