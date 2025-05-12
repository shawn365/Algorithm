from collections import Counter
def solution(array):
    counter = Counter(array).most_common(2)
    if len(counter) == 1:
        return counter[0][0]
    else:
        if counter[0][1] == counter[1][1]:
            return -1
        else:
            return counter[0][0]