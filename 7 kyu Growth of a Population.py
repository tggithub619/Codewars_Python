#https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python/me/best_practice

def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:
        p0 += p0 * percent / 100 + aug
        y += 1
    return y
48 similar code variations