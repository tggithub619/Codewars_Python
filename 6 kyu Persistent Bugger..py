#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python/5fbb5a301704d0002bdc3f24

def persistence(n):
    count = 0
    while n > 9:
        x = 1
        count += 1
        for i in str(n):
            x *= int(i)
        n=x
    return count

Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)