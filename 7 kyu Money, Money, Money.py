#https://www.codewars.com/kata/563f037412e5ada593000114/solutions/python/me/best_practice

def calculate_years(p, i, tax, d):
    y = 0
    while  p < d:
        p += p * i - p * i * tax
        y += 1
    return y