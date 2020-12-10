#https://www.codewars.com/kata/57829376a1b8d576640000d6

def trump_detector(trump_speech):
    trump_speech = trump_speech.lower()
    trumpVowel = 0
    vowels = "aeiou"
    if trump_speech[0] in vowels:
        vowelCount = 1
    else:
        vowelCount = 0
    for i in range(1, len(trump_speech)):
        if trump_speech[i-1] != trump_speech[i] and trump_speech[i] in vowels :
            vowelCount += 1
        if trump_speech[i-1] in vowels and trump_speech[i] == trump_speech[i-1]:
            trumpVowel += 1
    return(round(trumpVowel/vowelCount , 2))

def trump_detector(trump):
    trump = trump.lower()
    vowels = "aoieu"
    count_v = 0
    count_r = 0
    for i in range(1,len(trump)):
        if trump[i] in vowels and trump[i-1] != trump[i]:
            count_v+=1
        elif trump[i] in vowels and trump[i-1] == trump[i]:
            count_r+=1
    if trump[0] in vowels and trump[0] !=trump[1]:
        count_v+=1
    return round((count_r)/count_v,2) if count_v !=0 else 0