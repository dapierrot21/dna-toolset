# from DNAToolkit import *
# import random
# from utilities import coloring_nucleotides

# # Creating a random DNA sequence for testing:
# randon_dna_string = "".join([random.choice(nucleotides) for _ in range(50)])

# dnaString = validate_sequence(randon_dna_string)


# print(f"\nSequence: {coloring_nucleotides(dnaString)}\n")
# print(f"[1] + Sequence Length: {len(dnaString)}\n")
# print(
#     coloring_nucleotides(
#         f"[2] + Nucleotide Frequency: {count_nucleotide_frequency(dnaString)}\n"
#     )
# )
# print(
#     f"[3] + DNA/RNA Transcription: {transcription(coloring_nucleotides(dnaString))}\n"
# )
# print(
#     f"[4] + DNA String + Complement + Reverse Complement:\n5' {coloring_nucleotides(dnaString)} 3'"
# )
# print(f"   {''.join(['|' for c in range(len(dnaString))])}")
# print(
#     coloring_nucleotides(
#         f"3' {dna_reverse_complement(dnaString)[::-1]} 5' [Complement]"
#     )
# )
# print(
#     coloring_nucleotides(
#         f"5' {dna_reverse_complement(dnaString)} 3' [Reverse Complement]\n"
#     )
# )
# print(f"[5] + GC Content: {guanine_cytosine_content(dnaString)}%\n")
# print(
#     f"[6] + GC Content in Subsection k=5: {guanine_cytosine_content_subsequence(dnaString, k=5)}\n"
# )
# print(f"[7] + Aminoacids Sequence from DNA: {translate_sequence(dnaString)}\n")
# print(f"[8] + Codon Frequency (L): {codon_usage(dnaString, 'L')}\n")
# print("[9] + Reading Frames:")
# for frame in generate_reading_frames(dnaString):
#     print(frame)

# print("\n[10] + All proteins in 6 open reading frames:")
# for protein in all_proteins_from_other_reading_frames(dnaString, 0, 0, True):
#     print(f"{protein}")


from bio_sequence import BioSequence

test_dna_class = BioSequence()
test_dna_class.generate_random_sequence(40, "DNA")

print(test_dna_class.get_sequence_info())
# print(test_dna_class.get_sequence_biotype())


# test_dna_class.generate_random_sequence()
# print(test_dna_class.get_sequence_info())
print(test_dna_class.count_nucleotide_frequency())
print(test_dna_class.transcription())
# testing to make sure the original sequence did not change.
# print(test_dna_class.dna_sequence)
print(test_dna_class.dna_reverse_complement())
print(test_dna_class.guanine_cytosine_content())
print(test_dna_class.guanine_cytosine_content_subsequence(k=5))
print(test_dna_class.translate_sequence())
print(test_dna_class.codon_usage("P"))

for rf in test_dna_class.generate_reading_frames():
    print(rf)

print(
    test_dna_class.proteins_from_reading_frames(
        ["N", "M", "L", "Y", "I", "R", "M", "R", "M", "T", "T", "H", "_"]
    )
)

print(test_dna_class.all_proteins_from_other_reading_frames())
