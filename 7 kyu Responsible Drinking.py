#https://www.codewars.com/kata/5aee86c5783bb432cd000018/solutions/python/me/best_practice

def hydrate(drink_string):
    y = drink_string.split(' ')
    x = sum([int(el) for el in y if el.isdigit()] )
    return f"{x} glasses of water" if x>1 else '1 glass of water'
