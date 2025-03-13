def solution(rank, attendance):
    temp_list = []
    for i, v in enumerate(rank):
        if attendance[i] == True:
            temp_list.append([rank[i], i])
    sorted_list = sorted(temp_list)

    return 10000 * sorted_list[0][1] + 100 * sorted_list[1][1] + sorted_list[2][1]