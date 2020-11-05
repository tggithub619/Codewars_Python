#https://www.codewars.com/kata/5556282156230d0e5e000089/solutions/python

def DNAtoRNA(dna):
    return dna.replace('T', 'U')

def dna_to_rna(dna):
    res = ''
    for i in range(len(dna)):
        if dna[i] == "T":
            res += "U"
        else:
            res += dna[i]
    return res