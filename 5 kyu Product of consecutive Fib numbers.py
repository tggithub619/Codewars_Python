#https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python/5fbb5e66bed6c3000d5520a3

def productFib(prod):
    f1 = 0
    f2 = 1
    while 1 != 2:
        if f1 * f2 == prod:
            return [f1, f2, True]
        if f1 * f2 > prod:
            return [f1, f2, False]
        f2 += f1
        f1 = f2 - f1


test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])