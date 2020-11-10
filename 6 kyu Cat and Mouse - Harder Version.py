#https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf/train/python

def cat_mouse(x,j):
    c = x.find('C')
    d = x.find('D')
    m = x.find('m')
    res = ""
    if c==-1 or m==-1 or d==-1:
        return "boring without all three"
    if c > m:
        if d < c and d > m and m > c - j - 1:
            res = 'Protected!'
        elif m > c - j - 1:
            res = 'Caught!'
        else:
            res = 'Escaped!'
    elif c < m:
        if d > c and d < m and m < c + j + 1:
            res = 'Protected!'
        elif m < c + j + 1:
            res = 'Caught!'
        else:
            res = 'Escaped!'
    return res
