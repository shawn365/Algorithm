def solution(num, k):
    answer = -1
    if str(k) in str(num):
        answer = str(num).index(str(k)) + 1
        
    return answer