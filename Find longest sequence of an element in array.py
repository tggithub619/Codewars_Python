#https://www.codewars.com/kata/5f8dd79aa962b600335f7577


def longest_sequence(arr, elem):
    if arr == [] or elem not in arr:
        return 0
    a = []
    for el in arr:
        if el==elem:
            a.append(str(el))
        else:
            a.append(" ")
        s = (''.join(a)).split()
        s = [len(i)/len(str(elem)) for i in s]
    return max(s)