#https://www.codewars.com/kata/599bb194b7a047b04d000077/solutions/python/me/best_practice

def how_many_pizzas(n):
    pizza =  n ** 2 // 64
    slice =   n ** 2 % 64 // 8
    return f"pizzas: {pizza}, slices: {slice}"