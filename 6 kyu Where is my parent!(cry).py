#https://www.codewars.com/kata/58539230879867a8cd00011c/solutions/python

def find_children(d):
    return ''.join( sorted({c.upper() + c*( d.lower().count(c) -1) for c in d.lower()}))