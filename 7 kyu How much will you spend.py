#https://www.codewars.com/kata/585d7b4685151614190001fd/solutions/python

def get_total(costs, items, tax):
    s =0
    for el in items:
        if el in costs:
            s+= costs[el]
    print(s)
    return round(s + tax * s, 2)

#getTotal(costs, ['socks', 'shoes'], 0.09), 70.85)

def getTotal(costs, items, tax):
    gross_cost = 0
    for item in items:
        if item in costs.keys():
            gross_cost += costs[item]
    return round(gross_cost + tax * gross_cost,2)

def getTotal(costs, items, tax):
    return round(sum(costs.get(e, 0) for e in items) * (1 + tax), 2)