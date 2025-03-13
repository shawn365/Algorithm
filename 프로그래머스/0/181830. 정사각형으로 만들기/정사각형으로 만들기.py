def solution(arr):
    if len(arr) > len(arr[0]):
        for i in arr:
            while len(i) != len(arr):
                i.append(0)
    else:
        while len(arr) != len(arr[0]):
            arr.append([0] * len(arr[0]))
            
    return arr