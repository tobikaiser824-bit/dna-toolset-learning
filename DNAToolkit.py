# DNA Toolkit file for DNA sequence analysis and manipulation
Nucleotides =["A", "C", "G", "T"]

# Check the sequence to make sure it is a DNA String

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0} 
    #Dictionary to hold the frequency of each nucleotide dictionary is a fast hashmap -> instead of searching for a number like in a list it searches for a key in a dictionary which is faster 
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict