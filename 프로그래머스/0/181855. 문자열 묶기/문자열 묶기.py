from collections import Counter
def solution(strArr):
    cnt = Counter()
    for i in strArr:
        cnt[len(i)] += 1
        
    return max(cnt.values())