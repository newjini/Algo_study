def solution(hot, K):
    answer = 1
    scoville = len(hot)
    hot.sort()
    while(True):
        spicy = hot[0] + (hot[1] * 2)
        hot[0] = spicy
        hot.pop(1)
        hot.sort()

        if hot[0] >= K or len(hot) == 1:
            if hot[0] == K:
                answer -= 1
            break
        else:
            answer += 1

    if answer + 1 == scoville and spicy != K:
        answer = -1

    return answer