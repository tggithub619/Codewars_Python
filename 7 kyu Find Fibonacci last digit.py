#https://www.codewars.com/kata/56b7251b81290caf76000978
def get_last_digit(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, (a+b) % 10
    return a

def get_last_digit(index):
    f1 = 1
    f2 = 1
    f3 = 0
    count = 3
    while count <= index:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        count += 1
    print (index, f3)
    return f3%10