#https://www.codewars.com/kata/5f5daf1a209a64001183af9b/train/python

def make_chocolates(small, big, goal):
    for s in range(0, small + 1):
        for b in range(0, big + 1):
            if goal == s * 2 + b * 5:
                return s
    return -1   
