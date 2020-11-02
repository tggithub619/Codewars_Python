#https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python

def update_light(current):
    if current == 'green':
         return "yellow"
    elif current == 'red':
            return 'green'
    else:
            return 'red'


# return 'yellow' if current == 'green' else 'red' if current == 'yellow' else 'green'


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]