#https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0;