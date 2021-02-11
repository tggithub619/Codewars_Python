#https://www.codewars.com/kata/55caf1fd8063ddfa8e000018

def arithmetic_sequence_elements(a, r, n):
    x = []
    for i in range(n):
        x.append(a)
        a += r
    return ", ".join([str(el) for el in x])
def arithmetic_sequence_elements(a, r, n):
    s = ''
    for i in range(n):
        s +=', ' + str(a)
        a += r
    return s[2::]

# est.assert_equals(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
# test.assert_equals(arithmetic_sequence_elements(1, 0, 5), '1, 1, 1, 1, 1')
# test.assert_equals(arithmetic_sequence_elements(1, -3, 10), '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')

def arithmetic_sequence_elements(a, r, n):
    return ", ".join((str(a+r*i) for i in range(n)))