
s = "pPoooyY"


def solution(s):
    answer = False
    s = s.lower()
    pcnt = 0
    ycnt = 0
    for i in s:
        if i == "p":
            pcnt = pcnt + 1
        elif i == "y":
            ycnt = ycnt + 1
    if pcnt == ycnt or pcnt==0 and ycnt==0 :
        answer = True
    return answer

### 한줄쏘쓰
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')