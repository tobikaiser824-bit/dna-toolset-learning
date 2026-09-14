# DNA Toolset/Code testing file

from DNAToolkit import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range (29)]) # Generate a random DNA sequence of length 10   

print(validateSeq(rndDNAStr))   
print(countNucFrequency(rndDNAStr))