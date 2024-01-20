import collections
from sequences import *


# Checkig the sequence to make sure it is a DNA string.
def validate_sequence(dna_sequence):
    """Checkig the sequence to make sure it is a DNA string."""
    tmpsequence = dna_sequence.upper()
    for nucleotide in tmpsequence:
        if nucleotide not in nucleotides:
            return False
    return tmpsequence


# Count the amount of time a nucleotide appears in DNA Sequence.
def count_nucleotide_frequency(sequence):
    """Counting the amount of times a nucleotide appears in DNA Sequence."""
    temp_frequency_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in sequence:
        temp_frequency_dict[nucleotide] += 1
    return temp_frequency_dict
    # return dict(collections.Counter(sequence))


# Transcription: DNA --> RNA
def transcription(sequence):
    """Transcription: DNA --> RNA. Replacing Thymine with Uracil."""
    return sequence.replace("T", "U")


# Swapping adenine with thymine and quanine with cytosine. Reversing newly generated string.
def dna_reverse_complement(sequence):
    """Swapping adenine with thymine and quanine with cytosine. Reversing newly generated string."""
    return "".join([DNA_ReverseComplement[nucleotide] for nucleotide in sequence])[
        ::-1
    ]  # reverse
    # Pythonic approach,
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return sequence.translate(mapping)[::-1]


# GC Content in DNA/RNA sequence.
def guanine_cytosine_content(sequence):
    """GC Content in DNA/RNA sequence."""
    return round((sequence.count("C") + sequence.count("G")) / len(sequence) * 100)


# GC Content in DNA/RNA sub-sequence length k. k=20 by default.
def guanine_cytosine_content_subsequence(sequence, k=20):
    """GC Content in DNA/RNA sub-sequence length k. k=20 by default."""
    res = []
    for i in range(0, len(sequence) - k + 1, k):
        subsequence = sequence[i : i + k]
        res.append(guanine_cytosine_content(subsequence))
    return res


# Translates a DNA sequence into an aminoacid sequence.
def translate_sequence(sequence, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence."""
    return [
        DNA_Codons[sequence[pos : pos + 3]]
        for pos in range(init_pos, len(sequence) - 2, 3)
    ]


# Provides the frequency of each codon encoding a given aminoacid in a DNA sequence.
def codon_usage(sequence, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence."""
    temp_list = []

    for i in range(0, len(sequence) - 2, 3):
        if DNA_Codons[sequence[i : i + 3]] == aminoacid:
            temp_list.append(sequence[i : i + 3])

    frequency_dict = dict(collections.Counter(temp_list))
    total_weight = sum(frequency_dict.values())
    for seq in frequency_dict:
        frequency_dict[seq] = round(frequency_dict[seq] / total_weight, 2)
    return frequency_dict


# Generate the six reading frames of a DNA sequence, including the reverse complement.
def generate_reading_frames(sequence):
    """Generate the six reading frames of a DNA sequence, including the reverse complement."""
    six_frames = []
    six_frames.append(translate_sequence(sequence, 0))
    six_frames.append(translate_sequence(sequence, 1))
    six_frames.append(translate_sequence(sequence, 2))
    six_frames.append(translate_sequence(dna_reverse_complement(sequence), 0))
    six_frames.append(translate_sequence(dna_reverse_complement(sequence), 1))
    six_frames.append(translate_sequence(dna_reverse_complement(sequence), 2))
    return six_frames
