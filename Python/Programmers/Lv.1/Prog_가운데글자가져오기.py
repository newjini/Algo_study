
s = "qwer"

def solution(s):
    answer = ""
    lens = len(s)
    if lens % 2 == 0:
        answer = s[lens//2-1:lens//2+1]
    else:
        answer = s[lens//2]
    return answer

print(solution(s))

### 한줄쏘쓰
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

