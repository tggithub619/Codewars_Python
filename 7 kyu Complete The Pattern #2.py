#https://www.codewars.com/kata/55733d3ef7c43f8b0700007c/train/python

def pattern(n):
    return '\n'.join(''.join(map(str, list(range(n, i - 1, -1)))) for i in range(1, n + 1))

