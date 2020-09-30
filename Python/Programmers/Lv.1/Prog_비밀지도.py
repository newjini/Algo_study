def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        ans = bin(x | y)[2:]
        ans = ans.zfill(n)
        answer.append(ans)
    for i in range(len(answer)):
        answer[i] = answer[i].replace("1","#")
        answer[i] = answer[i].replace("0"," ")
        ### a.zfill(n) 문자열 타입에서 원하는 개수만큼 0 채우기

    return answer



print(solution(n=5,arr1=[9,20,28,18,11], arr2=[30,1,21,17,28]))
print(solution(n=6,arr1=[46,33,33,22,31,50], arr2=[27,56,19,14,14,10]))


### 한줄쏘쓰
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer