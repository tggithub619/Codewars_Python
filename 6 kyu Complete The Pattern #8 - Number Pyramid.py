#https://www.codewars.com/kata/5575ff8c4d9c98bc96000042

def pattern(n):
    wide = n * 2 - 1
    s = ''
    r = ''
    arr = []
    for x in range(1, n + 1):
        y = x % 10
        s += str(y)
        r = s[::-1][1:]
        arr.append((s + r).center(wide))

    return '\n'.join(arr)

#     1
#    121
#   12321
#  1234321
# 123454321

# Test.assertEquals(pattern(1),"1");
# Test.assertEquals(pattern(4),"   1   \n  121  \n 12321 \n1234321");
# Test.assertEquals(pattern(0),"");
# Test.assertEquals(pattern(-25),"");


