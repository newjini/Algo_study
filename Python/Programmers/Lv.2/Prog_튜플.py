def solution(s):
    answer = []
    
    s = s.split('},')
    nums = [] * len(s)
    for i in s:
        num = ''
        for j in i:            
            if j != '{' and j != '}':
                num += j
        
        nums.append(num)
        
    numbers = []
    for i in range(len(nums)):
        j = list(map(int, nums[i].split(',')))
        numbers.append(j)
    numbers = sorted(numbers, key=lambda x : len(x))
    for i in numbers:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer