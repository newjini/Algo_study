import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution(participant, completion):

    par_dict = {}
    for par in participant:
        if par in par_dict.keys():
            par_dict[par] =par_dict[par] + 1
        else:
            par_dict[par] = 1
    for com in completion:
        par_dict[com] = par_dict[com] - 1
        if par_dict[com] == 0:
            del(par_dict[com])
#            par_dict.pop(com)

    return list(par_dict.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

# if __name__ == '__main__':
#     print(solution(participant,completion))
