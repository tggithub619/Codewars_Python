#https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python

def validate_code(code):
    code = str(code)
    return code.startswith('1') or code.startswith('2') or code.startswith('3')

def validate_code(code):
    return str(code).startswith(('1', '2', '3'))