#https://www.codewars.com/kata/57ed56657b45ef922300002b

def broken(inp):
    inp = str(inp)
    res = ''
    for i in range(0, len(inp)):
        if inp[i] == '0' :
            res += '1'
        else:
            res += '0'
    return res

def broken(inp):
    return ''.join(['0' if i == '1' else '1' for i in inp])