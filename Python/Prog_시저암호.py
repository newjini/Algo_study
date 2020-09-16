



### 알파벳인거 빼고 소문자인지 대문자인지 else 인 경우로 나눌 수 있음
def solution(s, n):
    answer = ''

    ans = 'abcdefghijklmnopqrstuvwxyz'
    a = 0
    for i in s:
        if i.isalpha():
            a = ord(i) + n
            # if i.islower():

            if chr(a) > 'z':
                    a = a - len(ans)
            # else:
            if chr(a) > 'Z':
                    a = a - len(ans)
            answer = answer + chr(a)
        else:
            answer = answer + ' '
    return answer

print(solution(s="AB", n=1))
print(solution(s="z", n=1))
print(solution(s="a B Z", n=4))


### 한줄 쏘쓰
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)