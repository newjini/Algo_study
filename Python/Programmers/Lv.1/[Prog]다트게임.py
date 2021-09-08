def solution(dartResult):
    
    dart = []
    tmp = 0
    for idx, str in enumerate(dartResult):
    
        if str.isdigit() and idx != 0:
            # 10일 경우,
            if dartResult[idx] == '0' and dartResult[idx-1] == '1':
                continue
            dart.append(dartResult[tmp:idx])
            tmp = idx
    dart.append(dartResult[tmp:])
    
    ans = [0 for _ in range(3)]
    for idx, dar in enumerate(dart):
        res = 1
        for i, d in enumerate(dar):
            
            if d.isalpha():
                if d == 'S':
                    ans[idx] = int(ans[idx]) ** 1
                if d == 'D':
                    ans[idx] = int(ans[idx]) ** 2
                if d == 'T':
                    ans[idx] = int(ans[idx]) ** 3
            elif d.isdigit():
                if i != 0 and dar[i-1] =='1' and dar[i] == '0':
                    ans[idx] = 10
                    continue
                ans[idx] = d
            else:
                if d == '*':
                    for i in range(idx-1, idx+1):
                        ans[i] = int(ans[i]) * 2                        
                elif d == '#':
                    ans[idx] = int(ans[idx]) * -1

    answer = sum(ans)
    return answer