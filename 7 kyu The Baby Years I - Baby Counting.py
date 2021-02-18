#https://www.codewars.com/kata/5bc9951026f1cdc77400011c

def baby_count(x):
    x = x.lower()
    b = x.count("b") // 2
    a = x.count("a")
    y = x.count("y")

    return min(b, a, y) if min(b, a, y) > 0 else 'Where\'s the baby?!'

# Test.assert_equals(baby_count('baby'), 1)
# Test.assert_equals(baby_count('abby'), 1)
# Test.assert_equals(baby_count('baby baby baby'), 3)
# Test.assert_equals(baby_count('Why the hell are there so many babies?!'), 1)
# Test.assert_equals(baby_count('Anyone remember life before babies?'), 1)
# Test.assert_equals(baby_count('Happy babies boom ba by?'), 2)
# Test.assert_equals(baby_count('b a b y'), 1)
# Test.assert_equals(baby_count(''), 'Where\'s the baby?!')
# Test.assert_equals(baby_count('none here'), 'Where\'s the baby?!')

def baby_count(x):
    x = x.lower()
    return min(x.count('a'), x.count('b') // 2, x.count('y')) or "Where's the baby?!"