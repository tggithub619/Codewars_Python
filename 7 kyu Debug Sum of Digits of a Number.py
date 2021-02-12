#https://www.codewars.com/kata/563d59dd8e47a5ed220000ba

def get_sum_of_digits(num):
    sum = 0
    digits = str(num)
    for x in digits:
        sum += int(x)
    return sum

#test.assert_equals(get_sum_of_digits(123), 6)


