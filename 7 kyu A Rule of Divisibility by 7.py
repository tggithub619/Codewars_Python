#https://www.codewars.com/kata/55e6f5e58f7817808e00002e

def seven(m):
    count = 0
    while m > 99:
        m = m // 10 - (m % 10 * 2)
        count += 1
    return m, count

# test.assert_equals(seven(1603), (7, 2))
#         test.assert_equals(seven(371), (35, 1))
#         test.assert_equals(seven(483), (42, 1))
#         test.assert_equals(seven(483595), (28, 4))
