#https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python

def solve(eq):
    res = (eq.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split(' '))
    return ''.join(res[::-1])