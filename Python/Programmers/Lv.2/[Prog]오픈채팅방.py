def solution(record):
    order = []
    name = dict()
    for line in record:
        order.append(line.split())
    
    for i in range(len(order)):
        if order[i][0] == 'Enter':
            name[order[i][1]] = order[i][2]
        if order[i][0] == 'Change':
            name[order[i][1]] = order[i][2]

    answer = []
    for i in range(len(order)):
        if order[i][0] == 'Enter':
            answer.append(f'{name[order[i][1]]}님이 들어왔습니다.')
        elif order[i][0] == 'Leave':
            answer.append(f'{name[order[i][1]]}님이 나갔습니다.')
    
    
    return answer