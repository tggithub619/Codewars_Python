#https://www.codewars.com/kata/52755006cc238fcae70000ed

def christmas_tree(h):
    btm = h * 2 - 1
    s = ''
    for i in range(1, btm + 1, 2):
        s += ('*' * i).center(btm) + '\n'
    return s[:-1]


#     *
#    ***
#   *****
#  *******
# *********

# test.assert_equals(christmas_tree(0), '')
#         test.assert_equals(christmas_tree(1), '*')
#         test.assert_equals(christmas_tree(2), ' * \n***')
#         test.assert_equals(christmas_tree(3), '  *  \n *** \n*****')
#         test.assert_equals(christmas_tree(4), '   *   \n  ***  \n ***** \n*******')

def christmas_tree(n):
    return '\n'.join(("*"*(x*2+1)).center(n*2-1) for x in range(n))