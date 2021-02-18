#https://www.codewars.com/kata/5631213916d70a0979000066

def pattern(n):
    arr = ['1']
    for i in range(2, n+1):
        arr.append('1'+ "*" * (i-1) +str(i))
    return '\n'.join(arr)


def pattern(n):
    return '\n'.join(['1'] + ['1' + '*' * (i-1) + str(i) for i in range(2, n+1)])

# Test.assert_equals(pattern(3),"1\n1*2\n1**3")
# Test.assert_equals(pattern(7),"1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")
