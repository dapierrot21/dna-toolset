from DNAToolkit import *
import random
from utilities import coloring_nucleotides

# Creating a random DNA sequence for testing:
randon_dna_string = "".join([random.choice(nucleotides) for _ in range(50)])

dnaString = validate_sequence(randon_dna_string)


print(f"\nSequence: {coloring_nucleotides(dnaString)}\n")
print(f"[1] + Sequence Length: {len(dnaString)}\n")
print(
    coloring_nucleotides(
        f"[2] + Nucleotide Frequency: {count_nucleotide_frequency(dnaString)}\n"
    )
)
print(
    f"[3] + DNA/RNA Transcription: {transcription(coloring_nucleotides(dnaString))}\n"
)
print(
    f"[4] + DNA String + Complement + Reverse Complement:\n5' {coloring_nucleotides(dnaString)} 3'"
)
print(f"   {''.join(['|' for c in range(len(dnaString))])}")
print(
    coloring_nucleotides(
        f"3' {dna_reverse_complement(dnaString)[::-1]} 5' [Complement]"
    )
)
print(
    coloring_nucleotides(
        f"5' {dna_reverse_complement(dnaString)} 3' [Reverse Complement]\n"
    )
)
print(f"[5] + GC Content: {guanine_cytosine_content(dnaString)}%\n")
print(
    f"[6] + GC Content in Subsection k=5: {guanine_cytosine_content_subsequence(dnaString, k=5)}\n"
)
print(f"[7] + Aminoacids Sequence from DNA: {translate_sequence(dnaString)}\n")
print(f"[8] + Codon Frequency (L): {codon_usage(dnaString, 'L')}\n")
print(f"[9] + Reading Frames:")
for frame in generate_reading_frames(dnaString):
    print(frame)