#https://www.codewars.com/kata/571b2ee08d8c9c0d160014ec

def sexy_name(name):
    s = 0
    for el in name.upper():
        if el in SCORES:
            s+= SCORES[el]

    return 'NOT TOO SEXY' if s <= 60 else 'PRETTY SEXY' if  61 <= s <= 300 else 'VERY SEXY' if 301 <= s <= 599 else 'THE ULTIMATE SEXIEST'


def sexy_name(name):
    name_score = sum(SCORES.get(a, 0) for a in name.upper())
    if name_score >= 600:
        return 'THE ULTIMATE SEXIEST'
    elif name_score >= 301:
        return 'VERY SEXY'
    elif name_score >= 61:
        return 'PRETTY SEXY'
    return 'NOT TOO SEXY'