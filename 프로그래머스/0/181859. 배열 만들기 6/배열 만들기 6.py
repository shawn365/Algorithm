def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif i == answer[-1]:
            answer.pop()
        else:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
        
    return answer