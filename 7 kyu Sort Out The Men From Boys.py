#https://www.codewars.com/kata/5af15a37de4c7f223e00012d/solutions/python/me/best_practice

def men_from_boys(arr):
    arr = list(set(arr))
    men = sorted([x for x in arr if x % 2 == 0])
    boys = sorted([x for x in arr if x not in men], reverse = True)
    return men + boys