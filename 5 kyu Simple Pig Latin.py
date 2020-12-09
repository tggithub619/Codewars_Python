#https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    text=text.split(' ')
    s = []
    for i,el in enumerate(text):
        if el.isalpha():
            rest = el[1:]  + el[0]+ 'ay'
            s.append(rest)
        else:
            s.append(el)
    return ' '.join(s)


def pig_it(text):
    text = text.split(' ')
    s = []
    for i, el in enumerate(text):
        if el not in "/*-+,.;:!?":
            rest = el[1:] + el[0] + 'ay'
            s.append(rest)
        else:
            s.append(el)
    return ' '.join(s)
