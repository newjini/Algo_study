dir = [-3, 3, -1, 1] # 상 하 좌 우
nums = { 1 : (0,0) , 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 
        9:(2,2), 0:(3,1), '*':(3,0), '#':(3,2)}

def calDist(left, right, hand, now):
    ans = ''
    L = abs(nums[left][0] - nums[now][0]) + abs(nums[left][1] - nums[now][1])
    R = abs(nums[right][0] - nums[now][0]) + abs(nums[right][1] - nums[now][1])
    if L > R:
        ans = 'R'
    elif L < R:
        ans = 'L'
    elif L == R:
        if hand == "left":
            ans = 'L'
        else:
            ans = 'R'
    return ans

def solution(numbers, hand):
    global dir
    answer = ''
    left = "*"
    right = "#"
    for n in numbers:
        if n in (1,4,7):
            answer += 'L'
            left = n
        elif n in (3,6,9):
            answer += 'R'
            right = n
        else:
            res = calDist(left, right, hand, n)
            if res == 'L':
                left = n
            else:
                right = n
            answer += res     
            
    return answer