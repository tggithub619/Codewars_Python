#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    lst = []
    for i in range(len(s)):
        lst.append(s[i].upper() + s[i].lower()*i )
    return '-'.join(lst)