#https://www.codewars.com/kata/5750699bcac40b3ed80001ca/solutions/python/me/best_practice

def match(usefulness, months):
    return "Match!" if sum(usefulness) >= 0.85**months * 100 else "No match!"

def match(usefulness, months):
    x = 100
    s =  sum(usefulness)
    for i in range(0,months+1):
        if s >= x:
            return "Match!"
        else:
            x = x *0.85
    return "No match!"