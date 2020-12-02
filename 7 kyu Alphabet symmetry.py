#https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/solutions/python/me/best_practice

def count_str(s):
    count = 0
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i, el in enumerate(s):
        if i == a.index(el):
            count += 1
    return count


def solve(arr):
    arr = [el.lower() for el in arr]
    return [count_str(el) for el in arr]

