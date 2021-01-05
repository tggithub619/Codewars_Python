#https://www.codewars.com/kata/5e2aec959bce5c001f090c4d

def count_of_heads(init, n, swings):
    for i in range(1, swings + 1):
        n *= i
        init = init - 1 + n
    return init
