#https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

def clean_string(s):
    arr = []
    for el in s:
        if el != '#':
            arr.append(el)
        else:
            if arr:
                arr.pop()
    return ''.join(arr)

# Test.assert_equals(clean_string('abc#d##c'), "ac")
# Test.assert_equals(clean_string('abc####d##c#'), "" )
# Test.assert_equals(clean_string("#######"), "" )
# Test.assert_equals(clean_string(""), "" )