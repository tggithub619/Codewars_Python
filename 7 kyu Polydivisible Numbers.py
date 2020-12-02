#https://www.codewars.com/kata/5e4217e476126b000170489b/solutions/python/me/best_practice

def polydivisible(x):
    x = str(x)
    for i in range(1,len(x)+1):
        if int(x[:i]) % i:
            return False
    return True