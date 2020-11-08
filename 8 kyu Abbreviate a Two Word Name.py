#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    arr = name.split(' ')
    return f"{arr[0][0]}.{arr[1][0]}".upper()