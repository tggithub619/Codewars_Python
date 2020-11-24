#https://www.codewars.com/kata/57ba58d68dcd97e98c00012b/solutions/python/me/best_practice

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    return True


def prime_primes(n):
    count = 0
    s  = 0
    arr = [ i for i in range(2, n) if is_prime(i)]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            s += arr[i]/ arr[j]
            count += 1
    return count, int(s)