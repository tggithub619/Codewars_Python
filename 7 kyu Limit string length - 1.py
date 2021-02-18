#https://www.codewars.com/kata/5208fc3cb613bc725f000142

def solution(st, limit):
    return st if len(st) <= limit else st[:limit] + '...'

# test.assert_equals(solution('Testing String',3), 'Tes...')
#     test.assert_equals(solution('Testing String',8), 'Testing ...')
#     test.assert_equals(solution('Test', 10), 'Test')
#     test.assert_equals(solution('Test', 4), 'Test')

def solution(st, limit):
    return st[:limit] + '...' * (limit < len(st))