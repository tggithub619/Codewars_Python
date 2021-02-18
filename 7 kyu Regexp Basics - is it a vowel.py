#https://www.codewars.com/kata/567bed99ee3451292c000025

def is_vowel(s):
    return s.lower() in 'aeuio' and len(s)>0

# test.assert_equals(is_vowel(""), False)
# test.assert_equals(is_vowel("a"), True)
# test.assert_equals(is_vowel("E"), True)
# test.assert_equals(is_vowel("ou"), False)
# test.assert_equals(is_vowel("z"), False)
# test.assert_equals(is_vowel("lol"), False)

