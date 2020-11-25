#https://www.codewars.com/kata/574c5075d27783851800169e/train/python

def animals(heads, legs):
    chicken=(legs-2*heads)/2
    cow= heads-chicken
    if cow%1 !=0 or chicken%1 !=0:
        return 'No solutions'
    return (cow, chicken) if cow>=0 and chicken>=0 else 'No solutions'




def animals(heads, legs):
    for chicken in range(0, heads + 1):
        for cows in range(0, heads + 1):
            if chicken * 2 +cows * 4 == legs and chicken + cows == heads:
                return (chicken, cows)
    return 'No solutions'