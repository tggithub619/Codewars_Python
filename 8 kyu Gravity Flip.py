#https://www.codewars.com/kata/5f70c883e10f9e0001c89673/solutions/python/me/best_practice

def flip(d, a):
    return sorted(a, reverse=True) if d=='L' else sorted(a)
    # Do some magic