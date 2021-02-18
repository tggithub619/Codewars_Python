#https://www.codewars.com/kata/5856c5f7f37aeceaa100008e

def baubles_on_tree(baubles, branches):
    if branches ==0:
        return "Grandma, we will have to buy a Christmas tree first!"
    each = baubles//branches
    rest = baubles%branches
    arr = [each]*branches
    for i in range(rest):
        arr[i]+=1
    return arr

# Test.assert_equals(baubles_on_tree(5,5),[1,1,1,1,1])
# Test.assert_equals(baubles_on_tree(5,0),"Grandma, we will have to buy a Christmas tree first!")
# Test.assert_equals(baubles_on_tree(6,5),[2,1,1,1,1])
# Test.assert_equals(baubles_on_tree(50,9),[6,6,6,6,6,5,5,5,5])
# Test.assert_equals(baubles_on_tree(0,10),[0,0,0,0,0,0,0,0,0,0])