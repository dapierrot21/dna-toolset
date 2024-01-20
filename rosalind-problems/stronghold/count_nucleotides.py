import collections


# Count the amount of time a nucleotide appears in DNA Sequence.
def countNucleotideFrequency(sequence):
    tempFrequencyDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in sequence:
        tempFrequencyDict[nucleotide] += 1
    return tempFrequencyDict


dnaString = "GTCTCTAGTTCGCGCTCATGCATAGCACCCAGAGTATGGCGCCACCCAGCAGTGAGGAGTGCCGTTGCGTGGCTCGAGCACGAACTAAAAACTTGGGAGTCCGCGTTGGGGGGAACTAGGACTGGCAGGTCCCGGACAAGCAGAGTGAAGGCACGGCGGTGGACTCGCGCCAATGTATAACTATTTAATATTAGCTGCGACTCGTGTACCAAAGAAGACTCTAAAATCACTCCGCTAATATCTGATCTCCTTCGTTAACAGATGGGCAAGAACAGCTGATGCTAACTTGCCGAAAAAGCGCTTTCATCCCTCCAGAGGCTCCTCCAGGTACCATTCGGTCATGAAGATCGCGCCAAGCATGGCACGACTTCCTCCGGGCCGACATCGAGAGGCCCCTGCCGTAAGGGAATGGCTATCTCCAACGGACACATTAAACCGCCCGCGCTATCGTGGGTGCGAGATCAGTGTCGGCACATTGGAATAAGAGTCCAAAGGTTAACGGGGCAACTAACGGGACCCTAGGGACTTGCCGGCCCGCACGGACAAACAATCTTTGCCAAGCTCGTATTACGGAGAAGGATGTGATCTCCTTCGGTATACCTATGGGCGATTGAGCGTGCAAGCCTAAGGCTGTAAGGTTACCAAAGCCGTCTGTGTTGCTTCGATTACGGACTCCCTTGTAGAGGTTATGGCTTGTGTTGCCTGCCGTGACCTGGCGTAATTGAGGATTCGCTTTCTGGTGCAACTAAGCCCGCAGACGCAAGAAGTGCGCCCTTCCACCTCGGACCTCGTCAACCCTGAGGTGGGGATCAAGGCATGTACCAGAATGGATTACATGCGTCCAGACTGAGGCGGGACTTTTTCGACGAAGTATACAGGGTCAGAAATCAGTCGAATCATTAGCTACTGTGCGACTAGTCTCCATTCAAGCAGTGACTCG"
result = countNucleotideFrequency(dnaString)
print(" ".join([str(val) for key, val in result.items()]))
