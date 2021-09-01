import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    # 1) re 이용하는 법
#    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    
    # 2) 이용 안함.
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-", "_", "."]:
            answer += value
    new_id = answer
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4단계
    if new_id[0] == '.':
        if len(new_id) >= 2:
            new_id = new_id[1:]
        else:
            new_id = '.'
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5단계
    if len(new_id) == 0:
        new_id += 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id
    return answer