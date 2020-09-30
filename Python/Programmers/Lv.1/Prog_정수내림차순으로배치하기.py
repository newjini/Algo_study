def solution(n):
    ans = list(map(str, str(n)))
    ans.sort(reverse=True)

    return ''.join(ans)

print(solution(n=118372))

### 한줄쏘쓰
def solution_2(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

### 
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));