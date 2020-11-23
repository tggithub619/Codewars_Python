#https://www.codewars.com/users/TanyaG/completed_solutions

def reverse_factorial(num):
    count = 1
    while num > 1:
        count += 1
        num /= count

    return str(count) + "!" if num == 1 else "None"