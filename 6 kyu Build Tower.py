#https://www.codewars.com/kata/576757b1df89ecf5bd00073b/solutions/python/me/best_practice

def tower_builder(n):
    lst = []
    length = n * 2 - 1
    for i in range(1, n * 2, 2):
        lst.append((i * "*").center(length))

    return lst