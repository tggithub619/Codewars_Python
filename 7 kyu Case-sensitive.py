#https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8

def case_sensitive(s):
    res = s.islower() or len(s)==0
    y = []
    if res != True:
        y = [el for el in s if el.isupper()  ]
    return [res, y]



def case_sensitive(s):
    return [s.islower() or len(s)==0, [el for el in s if el.isupper()  ]]


# test.assert_equals(case_sensitive('asd'), [True, []])
# test.assert_equals(case_sensitive('cellS'), [False, ['S']])
# test.assert_equals(case_sensitive('z'), [True, []])
# test.assert_equals(case_sensitive(''), [True, []])