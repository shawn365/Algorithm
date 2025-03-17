def solution(score):
    answer = []
    avg_score = [sum(i) / 2 for i in score]
    sorted_avg_score = sorted(avg_score, reverse=True)
    for i in avg_score:
        answer.append(sorted_avg_score.index(i) + 1)
    
    return answer