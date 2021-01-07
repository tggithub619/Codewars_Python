#https://www.codewars.com/kata/563d54a7329a7af8f4000059

def build_row_text(ind, ch):
    s = ['| ']*9
    #print(ind, ch, s)
    s[ind] = '|'+ ch
    return "".join(s)+'|'

def build_row_text(index, character):
    str = ""
    for i in range(9):
        if i == index:
            str += "|" + character
        else: str += "| "
    return str + "|"