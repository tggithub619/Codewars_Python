#https://www.codewars.com/kata/590ee3c979ae8923bf00095b

def color_2_grey(colors):
    res = []
    for el1 in colors:
        res.append([[round(sum(el2) / 3)] * 3 for el2 in el1])

    return res


def color_2_grey(colors):
    res = []
    for el1 in colors:
        arr = []
        for el2 in el1:
            arr.append([round(sum(el2)/3)]*3)
        res.append(arr)
    return res