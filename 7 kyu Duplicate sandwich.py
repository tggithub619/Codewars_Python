#https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/python

def duplicate_sandwich(arr):
    res = []
    for i, el in enumerate(arr):
        if arr.count(el) == 2:
            res.append(i)
    return arr[res[0] + 1:res[1]]


def duplicate_sandwich(arr):
    res = [i for i, el in enumerate(arr) if arr.count(el)  == 2]
    return arr[res[0]+1:res[1]]