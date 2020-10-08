
def solution(number, k):
    stack = []
    for a, i in enumerate(number):
        while len(stack) > 0 and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1

        stack.append(i)
    if k > 0:
        for i in range(k):
            stack.pop()

    return ''.join(stack)




#print(solution(number="1924", k=2))
print(solution(number="999", k=2))
print(solution(number="111119", k=3))
#print(solution(number="1231234", k=3))
#print(solution(number="4177252841", k=4))

### 한줄쏘쓰
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)