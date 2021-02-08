#https://www.codewars.com/kata/552564a82142d701f5001228/solutions/python

def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)

# Test.assert_equals(discover_original_price(75,25),100)
# Test.assert_equals(discover_original_price(25,75),100)
# Test.assert_equals(discover_original_price(75.75,25),101)
# Test.assert_equals(discover_original_price(373.85,11.2),421)
# Test.assert_equals(discover_original_price(458.2,17.13),552.91)