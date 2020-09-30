def solution(phone_number):
    answer = ''
    answer = phone_number.replace(phone_number[:-4], "*"*len(phone_number[:-4]))



    return answer

print(solution(phone_number="01033334444"))
print(solution(phone_number="027778888"))


### 한줄쏘쓰
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

