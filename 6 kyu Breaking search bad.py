#https://www.codewars.com/kata/52cd53948d673a6e66000576/solutions/python/me/best_practice

def search(titles, term):
    return [el  for el in titles if term in el.casefold()]


def search(titles, term):
    return [ title for title in titles if term in title.lower() ]