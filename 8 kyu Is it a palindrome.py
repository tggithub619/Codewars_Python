#https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/solutions/python/me/best_practice

def is_palindrome(s):
    return s[::-1].lower() == s.lower()