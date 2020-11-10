#https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python

def initialize_names(name):
    lst= name.split(" ")
    if len(lst) > 2 :
        for i in range(1, len(lst)-1):
            lst[i] = lst[i][0: 1] +"."
#         m = name[name.find(" ")+1:1]
    return " ".join(lst)