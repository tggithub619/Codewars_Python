#https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/solutions/python/me/best_practice

def bingo(array):
    bingo = [2,7,9,14,15]
    return 'WIN' if len([el for el in bingo if el in array])==5 else'LOSE'

def bingo(array):
    return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"

def bingo(array):
    return "WIN" if all(i in array for i in [2,9,14,7,15]) else "LOSE"

def bingo(array):
    ctr = 0
    for i in [2, 9, 14, 7, 15]:
        if i in list(set(array)):
            ctr += 1
    if ctr == 5:
        return "WIN"
    else:
        return "LOSE"
    pass