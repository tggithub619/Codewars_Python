#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(w):
    if len(w) != 10:
        return False
    ns = 0
    we = 0
    for i,el in enumerate(w):
        if el == 'n':
            ns+= 1
        elif el == 's':
            ns -= 1
        elif el == 'w':
            we += 1
        elif el == 'e':
            we -= 1
    return ns == 0 and we == 0