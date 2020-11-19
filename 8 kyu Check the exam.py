#https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(a1, a2):
    score = 0
    for i in range(len(a1)):
        if a1[i] == a2[i]:
            score += 4
        elif a2[i] == "":
            score += 0
        elif a1[i] != a2[i]:
            score -= 1

    return 0 if score < 0 else score