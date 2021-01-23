#https://www.codewars.com/kata/57e35f1bc763b8ccce000038


import string

def check_password(s):
    s0 = 8<= len(s)<=20
    s1 = [el for el in s if el.isupper() ]
    s2 = [el for el in s if el.islower() ]
    s3 = [el for el in s if el.isdigit() ]
    s4 = [el for el in s if el in "!@#$%^&*?" ]
    s5 = [el for el in s if el not in string.ascii_letters + string.digits + "!@#$%^&*?"]
    return "valid" if s0 and s1 and s2 and s3 and s4 and  not s5 else "not valid"

def check_password(s):
    c1 = 8 <= len(s) <=20
    c2 = any([i.isupper() for i in s])
    c3 = any([i.islower() for i in s])
    c4 = any([i.isdigit() for i in s])
    c5 = any([i for i in s if i in '!@#$%^&*?'])
    c6 = not any([i for i in s if i not in '!@#$%^&*?' and not i.isupper() and not i.islower() and not i.isdigit()])
    return 'valid' if c1 and c2 and c3 and c4 and c5 and c6 else 'not valid'


def check_password(s):
    length = 8 <= len(s) <= 20
    upper = len([el for el in s if el.isupper()]) > 0
    lower = len([el for el in s if el.islower()]) > 0
    digit = len([el for el in s if el.isdigit()]) > 0
    special = len([el for el in s if el in "!@#$%^&*?"]) > 0
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    d = '0123456789'
    x = '!@#$%^&*?'
    only = len([el for el in s if el not in u + l + d + x]) == 0
    return "valid" if length and upper and lower and digit and special and only else "not valid"

# test.assert_equals(check_password(""), "not valid")
# test.assert_equals(check_password("password"), "not valid")
# test.assert_equals(check_password("P1@p"), "not valid")
# test.assert_equals(check_password("P1@pP1@p"), "valid")
# test.assert_equals(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"), "not valid")
# test.assert_equals(check_password("Paaaaaa222!!!"), "valid")