#https://www.codewars.com/kata/5959ec605595565f5c00002b/solutions/python/me/best_practice

def reverse_bits(n):
    return int(bin(n)[2:][::-1], 2)