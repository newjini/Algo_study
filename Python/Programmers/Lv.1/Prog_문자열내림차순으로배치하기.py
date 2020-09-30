
s = 'ABCabdc'

def solution(s):
    s = sorted(s)
    answer = ''
    up = []
    down = []
    for i in s:
        if i.isupper():
            up.append(i)
        else:
            down.append(i)
    down.reverse()
    up.reverse()
    answer = ''.join(down+up)
    return answer

print(solution(s))

### 한줄쏘쓰
def solution_2(s):
    return ''.join(sorted(s, reverse=True))