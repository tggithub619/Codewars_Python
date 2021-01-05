#https://www.codewars.com/kata/5676f07029da352ba2000065

def largest(n):
    print(n)
    if type(n) != int or n < 1:
        return False
    x = 10**n - 3
    while pow(2, x-1, x) != 1:
        print(x)
        x -= 2
    return x







def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True


def largest(n):
    print(n)
    if type(n) != int or n <= 0 :
        return False
    num = 10**n-1
    while not is_prime (num):
        num-= 1
    return num