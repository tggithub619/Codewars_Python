#https://www.codewars.com/kata/59e77930233243a7b7000026

def amaro_plan(pirate_num):
    gold = pirate_num *20
    my = gold - (pirate_num-1)//2
    arr = [my]
    for i in range(pirate_num-1):
        if i%2 != 0:
            arr.append(1)
        else:
            arr.append(0)
    return arr


def amaro_plan(pirate_num):
    gold = pirate_num*20
    mine = gold-(pirate_num-1)//2
    arr = [mine]
    for i in range(pirate_num-1):
        arr.append(1) if i%2!=0 else arr.append(0)
    return arr

# test.assert_equals(amaro_plan(2), [40, 0])
#         test.assert_equals(amaro_plan(3), [59, 0, 1])
#         test.assert_equals(amaro_plan(4), [79, 0, 1, 0])
#         test.assert_equals(amaro_plan(5), [98, 0, 1, 0, 1])
#

