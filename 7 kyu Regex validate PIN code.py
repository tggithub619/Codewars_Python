#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/solutions/python

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)