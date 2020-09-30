
a = 5
b = 24

def solution(a, b):
    answer = ''

    days = ["SUN", "MON", "TUE", "WED","THU", "FRI", "SAT"]
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = (days.index("FRI") + (sum(months[0:a-1])+b) % 7 ) % 7 - 1
    answer = days[answer]
    return answer

print(solution(a,b))