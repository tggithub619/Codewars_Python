#https://www.codewars.com/kata/596925532f709fccf3000077

def fizzbuzz_plusplus(nums, words):
    m =1
    for el in nums:
        m *=el
    arr = list(range(1,m+1))
    ar =[]
    for elem in arr:
        s = ''
        for i,num in enumerate(nums):
            if  elem % num == 0:
                s += words[i]
        if s =='':
            ar.append(elem)
        else:
            ar.append(s)
    return ar;
