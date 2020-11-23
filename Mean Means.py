#https://www.codewars.com/kata/57c6b44f58da9ea6c20003da/train/python

def geo_mean(nums, arith):
    miss = arith * (len(nums) + 1) - sum(nums)
    for el in nums:
        miss *= el
    geom = miss ** (1/(len(nums)+1))
    return geom
