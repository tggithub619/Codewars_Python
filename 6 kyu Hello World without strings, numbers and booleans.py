#https://www.codewars.com/kata/5b0148133e9715bf6f000154


def hi_all():
    one= len([[]])
    two = one +one
    three = one +two
    four = one +three
    five = one +four
    six = three +three
    seven = five +two
    eight = seven + one
    nine = five+four
    ten = five+five
    H = chr(ten * seven + two)
    e = chr(ten * ten + one)
    l = chr(ten * ten + eight)
    o = chr(ten * ten + ten + one)
    space = chr(ten * three + two)
    W = chr(ten * eight + seven)
    r = chr(ten * ten + ten + four)
    d = chr(ten * ten)
    return H + e + l + l + o + space + W + o + r + l + d

#test.assert_equals(hi_all(), "Hello World")