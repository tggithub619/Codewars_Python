#https://www.codewars.com/kata/57ee24e17b45eff6d6000164/solutions/python

def cat_mouse(x):
  return 'Escaped!' if len(x) > 5 else 'Caught!'

def cat_mouse(x):
    return 'Escaped!' if x.count('.') > 3 else 'Caught!'

def cat_mouse(x):
    c = x.index("C")
    m = x.index("m")
    return "Caught!" if abs(c-m) <= 4 else "Escaped!"