#https://www.codewars.com/kata/5effa412233ac3002a9e471d

def add(num1, num2):
    res = 0
    text = ''
    x = str(num1)
    y = str(num2)
    m = max(len(x),len(y))
    x= x.rjust(m, '0')
    y = y.rjust(m, '0')
    for i in range(len(x)):
        res = int(x[i])+int(y[i])
        text += str(res)
    return int(text)