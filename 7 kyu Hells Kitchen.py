#https://www.codewars.com/kata/57d1f36705c186d018000813

def gordon(a):
    print(a)
    a= a.upper().replace("A", "@")
    res = ''.join(["*" if el in 'EIOU' else el for el in a ])
    res = " ".join([el+ '!!!!' for el in res.split()])
    print(res)
    return res

#  test.assert_equals(gordon('What feck damn cake'), 'WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!')
#         test.assert_equals(gordon('are you stu pid'), '@R*!!!! Y**!!!! ST*!!!! P*D!!!!')
#         test.assert_equals(gordon('i am a chef'), '*!!!! @M!!!! @!!!! CH*F!!!!')
#         test.assert_equals(gordon('dont you talk tome'), 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!')
#         test.assert_equals(gordon('how dare you feck'), 'H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!')

def gordon(a):
    a=a.upper()
    a=a.replace(' ', '!!!! ')
    a=a.replace('A', '@')
    vowels = ['E', 'I', 'O', 'U']
    for each in vowels:
        a=a.replace(each, '*')
    return a + '!!!!'