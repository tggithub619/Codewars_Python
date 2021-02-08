#https://www.codewars.com/kata/57e2afb6e108c01da000026e

def expression_out(exp):
    num = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
    }

    op = {
        '+': 'Plus ',
        '-': 'Minus ',
        '*': 'Times ',
        '/': 'Divided By ',
        '**': 'To The Power Of ',
        '=': 'Equals ',
        '!=': 'Does Not Equal '
    }
    arr = exp.split()
    print(arr)

    return "That's not an operator!" if not arr[1] in op else f'{num[arr[0]]} {op[arr[1]]}{num[arr[2]]}'


op = {'+': 'Plus ', '-': 'Minus ', '*': 'Times ', '/': 'Divided By ', '**': 'To The Power Of ', '=': 'Equals ',
      '!=': 'Does Not Equal '}
num = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
       '9': 'Nine', '10': 'Ten'}


def expression_out(e):
    a, b, c = e.split()
    try:
        return num[a] + ' ' + op[b] + num[c]
    except:
        return 'That\'s not an operator!'