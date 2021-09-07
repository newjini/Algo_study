from bisect import bisect_left
from itertools import combinations

def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0,1,2,3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases
    

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))

    for key in all_people.keys():
        all_people[key].sort()
    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7])))
        else:
            answer.append(0)
    return answer


#### 효율성 무시한 해결 ####
# def solution(info, query):
#     answer = []
#     infos = []
#     for i in info:
#         infos.append(i.split(" "))
#     # 개발언어, 지원직군, 경력구분, 소울푸드
#     for que in query:
#         cnt = 0
#         q = []
#         aa = que.split(' ')
#         for a in aa:
#             if a != "and":
#                 q.append(a)
#             elif a.isdigit():
#                 q.append(a)
        
#         cnt = 0
#         for info in infos:
#             if int(q[4]) <= int(info[4]):
#                 if q[0] == '-' or q[0] == info[0]:
#                     if q[1] == '-' or q[1] == info[1]:
#                         if q[2] == '-' or q[2] == info[2]: 
#                             if q[3] == '-' or q[3] == info[3]:
#                                 cnt += 1
#         answer.append(cnt)
        
#     return answer
