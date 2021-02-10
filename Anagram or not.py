#https://www.codewars.com/kata/546274b0eaa31f79c9000d5d

def isAnagram(test, original):
  t = [x.lower() for x in test if x.isalnum()]
  o = [x.lower() for x in original if x.isalnum()]
  return sorted(t) == sorted(o)

# test.assert_equals(isAnagram("William Shakespeare","I am a weakish speller"), True)
# test.assert_equals(isAnagram("Silent","Listen"), True)
# test.assert_equals(isAnagram("Car","Cat"), False, "Car is not an anagram of Cat")
# test.assert_equals(isAnagram("12345","54321"), True)