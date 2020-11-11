#https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

def warn_the_sheep(q):
    if q[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {len(q[q.index('wolf') + 1:])}! You are about to be eaten by a wolf!"

def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'