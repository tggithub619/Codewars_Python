#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python/me/best_practice

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def descending_order(num):
    return int("".join(sorted(str(num))[::-1]))