#https://www.codewars.com/kata/52b23340c65ea422b1000045

def will_fit(present, box):
    p = sorted(present)
    b = sorted(box)
    print(p, b)
    f=b[0]-p[0]
    s=b[1]-p[1]
    l=b[2]-p[2]
    return f>0 and s>0 and l>0

def will_fit(present, box):
    p = sorted(present)
    b = sorted(box)
    return [b[i]-p[i] >1 for i in range(3)].count(True) ==3


def will_fit(present, box):
    p = sorted(present)
    b = sorted(box)
    return all([b[i]-p[i] >1 for i in range(3)])

# test.assert_equals(will_fit((10, 2, 4), (6, 4, 12)), True)
#     test.assert_equals(will_fit((1, 2, 3), (2, 1, 3)), False)