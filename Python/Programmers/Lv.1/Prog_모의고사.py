answers = [1,2,3,4,5]

def solution(answers):
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    answer =[0,0,0]
    max = -1
    ans = []
    for i in range(0,len(answers)):
        if no1[(i%len(no1))] == answers[(i%len(answers))]:
            answer[0] = answer[0] + 1
        if no2[(i%len(no2))] == answers[(i%len(answers))]:
            answer[1] = answer[1] + 1
        if no3[(i%len(no3))] == answers[(i%len(answers))]:
            answer[2] = answer[2] + 1

    for num, i in enumerate(answer):
        if max == i:
            max = i
            ans.append(num+1)
        if max < i:
            max = i
            del ans[:]
            ans.append(num+1)
    ans.sort()
    return ans

print(solution(answers))


