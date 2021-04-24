# def solution(numbers):
#     answer = ''
#     nums = {}
#     real = [0] * len(numbers)
#     for i in range(len(numbers)):
#         nums[i] = str(numbers[i])
    
#     for i in nums:
#         while len(nums[i]) <= 6:
#             nums[i] += nums[i]
#         real[i] = [numbers[i],int(nums[i][:7])] # *3 으로 푼 사람도 있슴
#     real = sorted(real, key= lambda x: -x[1])
#     for i in range(len(numbers)):
#         answer += str(real[i][0])
#     if int(answer) == 0:
#         answer = "0"
#     return answer
numbers = [6, 10, 2]
nums = list(map(str, numbers))
real = []
answer = ''
idx = 0
for i in nums:
    while len(i) <= 6:
        i += i
    string = i
    real.append([numbers[idx], int(string[:7])])
    idx += 1
real = sorted(real, key=lambda x:-x[1])
for i in range(len(real)):
    answer += str(real[i][0])
if int(answer) == 0:
    answer = "0"
print(answer)