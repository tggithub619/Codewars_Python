#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def areYouPlayingBanjo(name):
    return f"{name} plays banjo" if name.casefold().startswith("r") else f"{name} does not play banjo"