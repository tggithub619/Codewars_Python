#https://www.codewars.com/kata/58485a43d750d23bad0000e6/solutions/python/me/best_practice

def fizz_buzz_cuckoo_clock(time):
    h, m  = time.split(":")
    h, m = int(h), int(m)
    if h>= 13:
        h-=12
    if m == 0 :
        return ('Cuckoo ' * h).strip() if h > 0 else ("Cuckoo " *12).strip()
    elif m == 30:
        return "Cuckoo"
    elif m % 15 == 0 :
        return "Fizz Buzz"
    elif m % 5 == 0:
        return "Buzz"
    elif m % 3 == 0:
        return "Fizz"
    else :
        return "tick"