board = [[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = []

def putSolution(board, moves):
    cnt = 0
    for k in moves:
        for i in range(len(board)):
            if board[i][k-1] !=0:
                answer.append(board[i][k-1])
                if len(answer) > 1:
                    if answer[-1] == answer[-2]:
                        answer.pop()
                        answer.pop()
                        cnt = cnt + 2
                board[i][k-1] = 0
                break
    return cnt

print(putSolution(board,moves))