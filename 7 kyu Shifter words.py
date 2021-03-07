#https://www.codewars.com/kata/603b2bb1c7646d000f900083

def shifter(st):
    if len(st) ==0: return 0
    arr = st.split(' ')
    s1 = set("HINOSXZMW")
    count = 0
    for el in set(arr):
        if set(el) == set(el) & s1:
            count+= 1
    return count

# shifter("SOS IN THE HOME") == 2 # shifter words are "SOS" and "IN"
# shifter("WHO IS SHIFTER AND WHO IS NO") == 3 # shifter words are "WHO", "IS", "NO"
# shifter("TASK") == 0 # no shifter words
# shifter("") == 0 # no shifter words in empty string

