from collections import deque


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:
            progresses[i] = (100 - progresses[i]) // speeds[i] + 1
        else:
            progresses[i] = (100 - progresses[i]) // speeds[i]
    now = 0
    for i in range(len(progresses)):
        if progresses[now] < progresses[i]:
            answer.append(i-now)
            now = i
    answer.append(len(progresses)-now)
    return answer


# print(solution(progresses=[93,30,55],speeds=[1,30,5]))
print(solution(progresses=[95,90,99,99,80,99],speeds=[1,1,1,1,1,1]))
# print(solution(progresses=[40, 93, 30, 55, 60, 65],speeds=[60, 1, 30, 5 , 10, 7]))
# print(solution(progresses=[93, 30, 55, 60, 40, 65],speeds=[1, 30, 5 , 10, 60, 7]))


### 한줄쏘쓰
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]