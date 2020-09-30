s  = "33435"
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
    for i in s.lower():
        if i >= "a" and i <= "z":
            answer = False
    return answer

print(solution(s))


### 한줄쏘쓰
def solution2(s):
    return s.isdigit() and len(s) in (4,6)

