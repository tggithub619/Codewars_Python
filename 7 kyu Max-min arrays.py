#https://www.codewars.com/kata/5a090c4e697598d0b9000004/solutions/python/all/best_practice

def solve(arr):
    newarr = []
    arr = sorted(arr)
    while arr:
        newarr .append(arr[-1])
        arr.pop()
        if arr:
            newarr.append(arr[0])
            del arr[0]
        else :
            break
    return newarr

def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res