#strings = ["sun", "bed", "car"]
strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key=lambda x: x[n])
    
    return answer

### 한줄쏘쓰
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))
