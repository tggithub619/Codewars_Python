#https://www.codewars.com/kata/525f039017c7cd0e1a000a26/solutions/python/me/best_practice

def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    count = 0
    while str(n)[::-1] != str(n):
        n += int(str(n)[::-1])
        count += 1
    return count