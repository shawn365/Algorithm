def solution(polynomial):
    lst = polynomial.replace(" ", "").split("+")
    num = 0
    x = 0
    for i in lst:
        if i.isnumeric():
            num += int(i)
        else:
            if i[:-1]:
                x += int(i[:-1])
            else:
                x += 1

    if x > 0 and num > 0:
        return f"{x}x + {num}" if x > 1 else f"x + {num}"
    elif x > 0:
        return f"{x}x" if x > 1 else f"x"
    else:
        return f"{num}"