#https://www.codewars.com/kata/55c11989e13716e35f000013/solutions/python/me/best_practice

def add(a,b):
    a = [1 if el == "1" else 0 for el in a]
    b = [1 if el == "1" else 0 for el in b]
    n1 = sum([el * 2 **(len(a)-1-i) for i,el in enumerate(a)])
    n2 =  sum([el * 2 **(len(b)-1-i) for i,el in enumerate(b)])
    s = n1 + n2
    x = ''
    while s >=2:
        ln= s%2
        if ln ==0:
            x+= "0"
        else:
            x+="1"
        s= s//2
    x = x +"0" if s ==0 else x +"1"
    return x[::-1]