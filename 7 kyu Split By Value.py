#https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc

def split_by_value(k, elements):
    arr = []
    for el in elements:
        if el < k:
            arr.append(el)
    for el in elements:
        if el >= k:
            arr.append(el)
    return arr

#split_by_value(5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6])
