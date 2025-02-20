def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            if flag[i] == True:
                answer += [arr[i], arr[i]]
            else:
                answer.pop()

    return answer