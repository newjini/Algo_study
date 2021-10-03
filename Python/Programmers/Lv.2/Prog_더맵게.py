import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        if scoville[0] >= K:
            break
        
        if len(scoville) >= 2:
            fir = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)

            mix = fir + sec * 2
            heapq.heappush(scoville, mix)
            answer += 1
        else:
            answer = -1
            break
    
    return answer