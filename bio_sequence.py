from bio_structures import nucleotides, DNA_Codons
from utilities import coloring_nucleotides
import random
import collections


class BioSequence:
    """DNA sequence class. Default value: ATCG, DNA No label"""

    def __init__(self, dna_sequence="ATCG", sequence_type="DNA", label="No Label"):
        """Sequence initialzation and sequence validation."""
        self.dna_sequence = dna_sequence.upper()
        self.label = label
        self.sequence_type = sequence_type
        self.is_valid = self.__validate_sequence()

        if not self.is_valid:
            raise ValueError(
                f"Provided data does not seem to be a correct {self.sequence_type} sequence."
            )

    def __validate_sequence(self):
        """Checkig the sequence to make sure it is a DNA string."""
        return set(nucleotides).issuperset(self.dna_sequence)

    def get_sequence_biotype(self):
        """Returns sequence type."""
        return self.sequence_type

    def get_sequence_info(self):
        """Returns Sequence Information"""
        return f"[Label]: {self.label}\n[Sequence]: {coloring_nucleotides(self.dna_sequence)}\n[Biotype]: {self.sequence_type}\n[Sequence Length]: {len(self.dna_sequence)}"

    def generate_random_sequence(self, length=10, sequence_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        sequence = "".join(random.choice(nucleotides) for _ in range(length))
        self.__init__(sequence, sequence_type, "Randomly generated sequence.")

    def count_nucleotide_frequency(self):
        """Counting the amount of times a nucleotide appears in DNA Sequence."""
        return dict(collections.Counter(self.dna_sequence))

    def transcription(self):
        """Transcription: DNA --> RNA. Replacing Thymine with Uracil."""
        return coloring_nucleotides(self.dna_sequence.replace("T", "U"))

    def dna_reverse_complement(self):
        """Swapping adenine with thymine and quanine with cytosine. Reversing newly generated string."""
        if self.sequence_type == "DNA":
            mapping = str.maketrans("ATCG", "TAGC")
        else:
            mapping = str.maketrans("AUCG", "TAGC")
        return self.dna_sequence.translate(mapping)[::-1]

    def guanine_cytosine_content(self):
        """GC Content in DNA/RNA sequence."""
        return round(
            (self.dna_sequence.count("C") + self.dna_sequence.count("G"))
            / len(self.dna_sequence)
            * 100
        )

    def guanine_cytosine_content_subsequence(self, k=20):
        """GC Content in DNA/RNA sub-sequence length k. k=20 by default."""
        res = []
        for i in range(0, len(self.dna_sequence) - k + 1, k):
            subsequence = self.dna_sequence[i : i + k]
            res.append(
                round(
                    (subsequence.count("C") + subsequence.count("G"))
                    / len(subsequence)
                    * 100
                )
            )
        return res

    def translate_sequence(self, init_pos=0):
        """Translates a DNA sequence into an aminoacid sequence."""
        return [
            DNA_Codons[self.dna_sequence[pos : pos + 3]]
            for pos in range(init_pos, len(self.dna_sequence) - 2, 3)
        ]

    def codon_usage(self, aminoacid):
        """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence."""
        temp_list = []

        for i in range(0, len(self.dna_sequence) - 2, 3):
            if DNA_Codons[self.dna_sequence[i : i + 3]] == aminoacid:
                temp_list.append(self.dna_sequence[i : i + 3])

        frequency_dict = dict(collections.Counter(temp_list))
        total_weight = sum(frequency_dict.values())
        for seq in frequency_dict:
            frequency_dict[seq] = round(frequency_dict[seq] / total_weight, 2)
        return frequency_dict

    def generate_reading_frames(self):
        """Generate the six reading frames of a DNA sequence, including the reverse complement."""
        six_frames = []
        six_frames.append(self.translate_sequence(0))
        six_frames.append(self.translate_sequence(1))
        six_frames.append(self.translate_sequence(2))

        temp_sequence = BioSequence(self.dna_reverse_complement(), self.sequence_type)
        six_frames.append(temp_sequence.translate_sequence(0))
        six_frames.append(temp_sequence.translate_sequence(1))
        six_frames.append(temp_sequence.translate_sequence(2))

        del temp_sequence
        return six_frames

    def proteins_from_reading_frames(self, aminoacid_sequence):
        """Compute all possible proteins in an aminoacid sequence and return a list of possible proteins."""
        current_protein = []
        proteins = []
        for aminoacid in aminoacid_sequence:
            if aminoacid == "_":
                # STOP accumulating amino acids if _ - STOP was found.
                if current_protein:
                    for protein in current_protein:
                        proteins.append(protein)
                    current_protein = []
            else:
                # START accumulating amino acids if M - START was found.
                if aminoacid == "M":
                    current_protein.append("")
                for i in range(len(current_protein)):
                    current_protein[i] += aminoacid
        return proteins

    def all_proteins_from_other_reading_frames(
        self, start_read_pos=0, end_read_pos=0, ordered=False
    ):
        """Compute all possible proteins for all open reading frames."""
        # Protein Search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2
        # API can be used to pull protein info.
        if end_read_pos > start_read_pos:
            temp_sequence = BioSequence(
                self.dna_sequence[start_read_pos:end_read_pos], self.sequence_type
            )
            reading_frames = temp_sequence.generate_reading_frames()
        else:
            reading_frames = self.generate_reading_frames()

        results = []
        for reading_frame in reading_frames:
            proteins = self.proteins_from_reading_frames(reading_frame)
            for protein in proteins:
                results.append(protein)

        if ordered:
            return sorted(results, key=len, reverse=True)
        return results
