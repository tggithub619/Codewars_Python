#https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69/train/python

def is_in_middle(seq):
    while len(seq) >= 3:
        if seq == 'abc' or seq[1:] == 'abc' or seq[:-1] == 'abc':
            return True
        seq = seq[1:-1]
    return False

def is_in_middle(seq):
    while len(seq) > 4:
        seq = seq[1:-1]
    if 'abc' in seq:
        return True
    return False

def is_in_middle(s):
    while len(s)>4:
        s = s[1:-1]
    return 'abc' in s