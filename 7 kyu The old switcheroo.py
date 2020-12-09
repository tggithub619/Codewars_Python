#https://www.codewars.com/kata/55d410c492e6ed767000004f

def vowel_2_index(string):
    return ''.join(x if x.lower() not in 'aeuio' else str(n + 1) for n,x in enumerate(string))


def vowel_2_index(string):
    s = ''
    for i, el in enumerate(string):
        if el.lower() in 'aeuio':
            s += str(i + 1)
        else:
            s += el
    return s


