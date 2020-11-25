#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/solutions/python/me/best_practice

def find_needle(h):
    x = h.index("needle")
    return f"found the needle at position {x}" if 'needle' in h else -1