#https://www.codewars.com/kata/55733d3ef7c43f8b0700007c/train/python

def pattern(n):
    return '\n'.join(''.join(map(str, list(range(n, i - 1, -1)))) for i in range(1, n + 1))

def pattern(n):
    result = []
    for i in range(n, 0, -1):
        string = ""
        for j in range(n, n-i, -1):
             string += str(j)
        result.append(string)
    return "\n".join(result)

def pattern(n):
    arr=[]
    for i in range(1,n+1):
        arr.append(list(range(n,i-1,-1)))
    for i in range(len(arr)):
        arr[i] = "".join([str(el) for el in arr[i]])
    return "\n".join(el for el in arr)

