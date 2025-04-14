def solution(s):
    temp = []
    for i in s.split(" "):
        if i == "Z":
            temp.pop()
        else:
            temp.append(int(i))
    return sum(temp)