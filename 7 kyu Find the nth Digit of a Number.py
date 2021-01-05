#https://www.codewars.com/kata/577b9960df78c19bca00007e

def find_digit(num, nth):
    if num < 0 : num = -num
    if nth <= 0: return -1
    s =  str(num)[::-1]
    if nth > len(str(num)):
        return 0
    return int(s[nth-1])