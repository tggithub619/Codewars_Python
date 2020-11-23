#https://www.codewars.com/kata/515e271a311df0350d00000f/solutions/python


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

def square_sum(numbers):
    res = 0
    for i in range(len(numbers)):
        res +=  numbers[i]**2
    return res