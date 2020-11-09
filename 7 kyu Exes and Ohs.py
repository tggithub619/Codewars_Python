#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    return s.casefold().count("o") == s.casefold().count("x")