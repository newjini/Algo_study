

import copy

def solution(s):
    answer = ''
    ans = list(s.split())
    word = []
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if j % 2 == 0:
                word += ans[i][j].upper()
            else:
                word += ans[i][j].lower()

    for i in range(len(s)):
        if s[i] == ' ':
            word.insert(i,' ')


    return ''.join(list(word))


print(solution(s="try hello world"))


### 한줄쏘쓰
def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])