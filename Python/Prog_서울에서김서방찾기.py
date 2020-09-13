seoul = ["Jane", "Kim"]

def solution(seoul):
    for num, i in enumerate(seoul):
        if i == "Kim":
            answer = "김서방은 %d에 있다" % num
    return answer
print(solution(seoul))


### 한줄쏘쓰
def hansol(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(hansol(seoul))