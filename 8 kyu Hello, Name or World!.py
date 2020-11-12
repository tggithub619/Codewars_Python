#https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python

def hello(name):
    return f"Hello, {name.lower().capitalize()}!" if len(name)>0 else "Hello, World!"

def hello(name = None):
    return "Hello, World!" if name == "" or name == None else f"Hello, {name.title()}!"

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"