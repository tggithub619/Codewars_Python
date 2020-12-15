#https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc

def read_zalgo(zalgotext):
    return "".join([c for c in zalgotext if c.isascii()])


import string


def read_zalgo(zalgotext):
    s0 = [el for el in zalgotext if el in string.ascii_letters + string.punctuation + ' ']

    return ''.join(s0)
