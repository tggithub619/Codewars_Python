#https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return a * 50 + 6


def problem(a):
    return 'Error' if type(a) is str else a * 50 + 6

def problem(a):
    return 'Error' if type(a) == str else a*50+6