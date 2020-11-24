#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    arr = sorted(arr)
    return arr[0] if arr[0] != arr[1] else arr[-1]