#https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    sum = 0
    for el in arr:
        if el > 0:
            sum = sum + el
    return sum


def positive_sum(arr):
    # Your code here
  return sum([x for x in arr if x > 0])