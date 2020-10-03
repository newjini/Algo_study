from math import gcd

def solution(w,h):
    r = gcd(w,h)
    if w < h:
        w, h = h, w


    return w*h - (w + h - r)





print(solution(w=8,h=12))
print(solution(w=4,h=3))
print(solution(w=1,h=1))