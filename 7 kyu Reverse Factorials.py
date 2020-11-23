#https://www.codewars.com/kata/58067088c27998b119000451/train/python/5fbb383be7fb84001d39ccf3

def reverse_factorial(num):
    count = 1
    while num > 1:
        count += 1
        num /= count

    return str(count) + "!" if num == 1 else "None"

test.assert_equals(reverse_factorial(120), '5!')
test.assert_equals(reverse_factorial(3628800), '10!')
test.assert_equals(reverse_factorial(150), 'None')